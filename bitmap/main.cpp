#include <fstream>
#include <iostream>
#include <cstdio>


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

static void print_headers(const BitmapHeaders& h) {
    std::cout << "2b headers.bitmap_signature : " << h.bitmap_signature[0] << h.bitmap_signature[1] << std::endl;
    std::cout << "4b headers.bitmap_file_size : " << h.bitmap_file_size << std::endl;
    std::cout << "4b headers.bitmap_reserved : " << h.bitmap_reserved << std::endl;
    std::cout << "4b headers.bitmap_data_offset : " << h.bitmap_data_offset << std::endl;
    std::cout << "4b headers.bitmap_info_header_size : " << h.bitmap_info_header_size << std::endl;
    std::cout << "4b headers.bitmap_width : " << h.bitmap_width << std::endl;
    std::cout << "4b headers.bitmap_height : " << h.bitmap_height << std::endl;
    std::cout << "2b headers.bitmap_planes : " << h.bitmap_planes << std::endl;
    std::cout << "2b headers.bitmap_bits_per_pixel : " << h.bitmap_bits_per_pixel << std::endl;
    std::cout << "4b headers.bitmap_compression : " << h.bitmap_compression << std::endl;
    std::cout << "4b headers.bitmap_image_size : " << h.bitmap_image_size << std::endl;
    std::cout << "4b headers.bitmap_XpixelsPerM : " << h.bitmap_XpixelsPerM << std::endl;
    std::cout << "4b headers.bitmap_YpixelsPerM : " << h.bitmap_YpixelsPerM << std::endl;
    std::cout << "4b headers.bitmap_ColorsUsed : " << h.bitmap_ColorsUsed << std::endl;
    std::cout << "4b headers.bitmap_ColorsImportant : " << h.bitmap_ColorsImportant << std::endl;
}

int main(const int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "image.bmp";

    BitmapHeaders headers {};

    // 54 байта файла читаем сразу в структуру
    if (!load_file_bytes(path, reinterpret_cast<unsigned char*>(&headers), sizeof(headers))) {
        printf("Failed to load file \n: %s", path);
        return 1;
    }
    bool check_signature = (headers.bitmap_signature[0] == 'B' && headers.bitmap_signature[1] == 'M');
    if (!check_signature) {
        printf("Not a BMP file \n: %s", path);
        return 1;
    }

    print_headers(headers);

    if (headers.bitmap_bits_per_pixel != 24 || headers.bitmap_compression != 0) {
        printf("Only uncompressed 24-bit BMP is supported\n");
        return 1;
    }

    const int w = headers.bitmap_width;
    const int h = headers.bitmap_height;

    const int row_size = (w * 3 + 3) / 4 * 4;
    const int data_size = row_size * h;

    unsigned char* pixels = new unsigned char[data_size];
    if (!load_file_bytes(path, pixels, data_size, headers.bitmap_data_offset)) {
        printf("Failed to read pixel data\n");
        delete[] pixels;
        return 1;
    }

    unsigned char* bottom_left  = pixels;
    unsigned char* bottom_right = pixels + (w - 1) * 3;
    unsigned char* upper_left   = pixels + (h - 1) * row_size;
    unsigned char* upper_right  = pixels + (h - 1) * row_size + (w - 1) * 3;

    printf("Top-left:     R: %d G: %d B: %d\n", upper_left[2], upper_left[1], upper_left[0]);
    printf("Top-right:    R: %d G: %d B: %d\n", upper_right[2], upper_right[1], upper_right[0]);
    printf("Bottom-left:  R: %d G: %d B: %d\n", bottom_left[2], bottom_left[1], bottom_left[0]);
    printf("Bottom-right: R: %d G: %d B: %d\n", bottom_right[2], bottom_right[1], bottom_right[0]);

    delete[] pixels;
    return 0;
}
