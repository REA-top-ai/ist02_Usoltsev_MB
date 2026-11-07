#include <fstream>
#include <iostream>
#include <cstdio>
#include <stdexcept>
#include <string>

#define HEADERS_SIZE 54

struct __attribute__((packed)) BitmapHeaders {
    char  bitmap_signature[2];
    int   bitmap_file_size;
    int   bitmap_reserved;
    int   bitmap_data_offset;
    int   bitmap_info_header_size;
    int   bitmap_width;
    int   bitmap_height;
    short bitmap_planes;
    short bitmap_bits_per_pixel;
    int   bitmap_compression;
    int   bitmap_image_size;
    int   bitmap_XpixelsPerM;
    int   bitmap_YpixelsPerM;
    int   bitmap_ColorsUsed;
    int   bitmap_ColorsImportant;
};


static bool load_file_bytes(const char* path, unsigned char* headers,
                            const int size, const int pos = 0) {
    std::ifstream file(path, std::ios::binary);
    if (!file) {
        return false;
    }
    file.seekg(pos);
    file.read(reinterpret_cast<char*>(headers), size);
    return static_cast<bool>(file);
}

class Bitmap {
public:
    explicit Bitmap(const char* path) {
        static_assert(sizeof(Pixel) == 3, "pixel must be exactly 3 bytes (B, G, R)");
        static_assert(sizeof(BitmapHeaders) == HEADERS_SIZE, "BMP headers must be 54 bytes");

        if (!load_file_bytes(path, reinterpret_cast<unsigned char*>(&headers), HEADERS_SIZE)) {
            throw std::runtime_error(std::string("Failed to load file: ") + path);
        }

        bool check_signature = (headers.bitmap_signature[0] == 'B' && headers.bitmap_signature[1] == 'M');
        if (!check_signature) {
            throw std::runtime_error(std::string("Not a BMP file: ") + path);
        }

        if (headers.bitmap_bits_per_pixel != 24 || headers.bitmap_compression != 0) {
            throw std::runtime_error("Only uncompressed 24-bit BMP is supported");
        }

        const int w = headers.bitmap_width;
        const int h = headers.bitmap_height;

        row_size = (w * static_cast<int>(sizeof(Pixel)) + 3) / 4 * 4;
        const int data_size = row_size * h;

        pixels = new unsigned char[data_size];
        if (!load_file_bytes(path, pixels, data_size, headers.bitmap_data_offset)) {
            delete[] pixels;
            pixels = nullptr;
            throw std::runtime_error("Failed to read pixel data");
        }
    }

    ~Bitmap() {
        delete[] pixels;
    }

    Bitmap(const Bitmap&) = delete;
    Bitmap& operator=(const Bitmap&) = delete;

    void print_headers() const {
        std::cout << "2b headers.bitmap_signature : " << headers.bitmap_signature[0] << headers.bitmap_signature[1] << std::endl;
        std::cout << "4b headers.bitmap_file_size : " << headers.bitmap_file_size << std::endl;
        std::cout << "4b headers.bitmap_reserved : " << headers.bitmap_reserved << std::endl;
        std::cout << "4b headers.bitmap_data_offset : " << headers.bitmap_data_offset << std::endl;
        std::cout << "4b headers.bitmap_info_header_size : " << headers.bitmap_info_header_size << std::endl;
        std::cout << "4b headers.bitmap_width : " << headers.bitmap_width << std::endl;
        std::cout << "4b headers.bitmap_height : " << headers.bitmap_height << std::endl;
        std::cout << "2b headers.bitmap_planes : " << headers.bitmap_planes << std::endl;
        std::cout << "2b headers.bitmap_bits_per_pixel : " << headers.bitmap_bits_per_pixel << std::endl;
        std::cout << "4b headers.bitmap_compression : " << headers.bitmap_compression << std::endl;
        std::cout << "4b headers.bitmap_image_size : " << headers.bitmap_image_size << std::endl;
        std::cout << "4b headers.bitmap_XpixelsPerM : " << headers.bitmap_XpixelsPerM << std::endl;
        std::cout << "4b headers.bitmap_YpixelsPerM : " << headers.bitmap_YpixelsPerM << std::endl;
        std::cout << "4b headers.bitmap_ColorsUsed : " << headers.bitmap_ColorsUsed << std::endl;
        std::cout << "4b headers.bitmap_ColorsImportant : " << headers.bitmap_ColorsImportant << std::endl;
    }

    void print_corners() const {
        if (pixels == nullptr) {
            return;
        }
        const int w = headers.bitmap_width;
        const int h = headers.bitmap_height;

        const unsigned char* bottom_left  = pixels;
        const unsigned char* bottom_right = pixels + (w - 1) * 3;
        const unsigned char* upper_left   = pixels + (h - 1) * row_size;
        const unsigned char* upper_right  = pixels + (h - 1) * row_size + (w - 1) * 3;

        print_pixel("Top-left:    ", upper_left);
        print_pixel("Top-right:   ", upper_right);
        print_pixel("Bottom-left: ", bottom_left);
        print_pixel("Bottom-right:", bottom_right);
    }

private:
    struct Pixel {
        unsigned char b;
        unsigned char g;
        unsigned char r;
    };

    static void print_pixel(const char* name, const unsigned char* p) {
        printf("%s R: %d G: %d B: %d\n", name, p[2], p[1], p[0]);
    }

    BitmapHeaders headers {};
    unsigned char* pixels = nullptr;
    int row_size = 0;
};

int main(const int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "image.bmp";

    try {
        Bitmap bitmap(path);
        bitmap.print_headers();
        bitmap.print_corners();
    } catch (const std::exception& e) {
        printf("%s\n", e.what());
        return 1;
    }

    return 0;
}