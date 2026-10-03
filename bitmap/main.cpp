#include <fstream>
#include <iostream>


using namespace std;
static constexpr int HEADERS_SIZE = 54;

struct BitmapHeaders {
    int bitmap_file_size;
    int bitmap_reserved;
    int bitmap_data_offset;
    int bitmap_info_header_size;
    int bitmap_width;
    int bitmap_height;
    short bitmap_planes;
    short bitmap_bits_per_pixel;
    int bitmap_compression;
    int bitmap_image_size;
    int bitmap_XpixelsPerM;
    int bitmap_YpixelsPerM;
    int bitmap_ColorsUsed;
    int bitmap_ColorsImportant;
};

struct VPixel {
    unsigned char b, g, r;
};


static int read_int(const unsigned char* bytes) {
    return bytes[0] | (bytes[1] << 8) | (bytes[2] << 16) | (bytes[3] << 24);
}

static short read_short(const unsigned char* bytes) {
    return static_cast<short>(bytes[0] | (bytes[1] << 8));
}

static bool check_signature(const unsigned char* sign) {
    return sign[0] == 'B' && sign[1] == 'M';
}

static bool load_raw_file_data(const char* path, unsigned char* file_data, const int size, const int pos = 0) {
    ifstream file(path, ios::binary);
    if (!file) { return false; }
    file.seekg(pos);
    file.read(reinterpret_cast<char*>(file_data), size);
    return static_cast<int>(file.gcount()) == size;
}

static void map_header(unsigned char const* source, BitmapHeaders& dest) {
    dest.bitmap_file_size = read_int(source + 2);
    dest.bitmap_reserved = read_int(source + 6);
    dest.bitmap_data_offset = read_int(source + 10);
    dest.bitmap_info_header_size = read_int(source + 14);
    dest.bitmap_width = read_int(source + 18);
    dest.bitmap_height = read_int(source + 22);
    dest.bitmap_planes = read_short(source + 26);
    dest.bitmap_bits_per_pixel = read_short(source + 28);
    dest.bitmap_compression = read_int(source + 30);
    dest.bitmap_image_size = read_int(source + 34);
    dest.bitmap_XpixelsPerM = read_int(source + 38);
    dest.bitmap_YpixelsPerM = read_int(source + 42);
    dest.bitmap_ColorsUsed = read_int(source + 46);
    dest.bitmap_ColorsImportant = read_int(source + 50);
}

static void print_bitmap_headers(const BitmapHeaders& h) {
    cout << "4b bitmap_file_size : " << h.bitmap_file_size << '\n'
          << "4b bitmap_reserved : " << h.bitmap_reserved << '\n'
          << "4b bitmap_data_offset : " << h.bitmap_data_offset << '\n'
          << "4b bitmap_info_header_size : " << h.bitmap_info_header_size << '\n'
          << "4b bitmap_width : " << h.bitmap_width << '\n'
          << "4b bitmap_height : " << h.bitmap_height << '\n'
          << "2b bitmap_planes : " << h.bitmap_planes << '\n'
          << "2b bitmap_bits_per_pixel : " << h.bitmap_bits_per_pixel << '\n'
          << "4b bitmap_compression : " << h.bitmap_compression << '\n'
          << "4b bitmap_image_size : " << h.bitmap_image_size << '\n'
          << "4b bitmap_XpixelsPerM : " << h.bitmap_XpixelsPerM << '\n'
          << "4b bitmap_YpixelsPerM : " << h.bitmap_YpixelsPerM << '\n'
          << "4b bitmap_ColorsUsed : " << h.bitmap_ColorsUsed << '\n'
          << "4b bitmap_ColorsImportant : " << h.bitmap_ColorsImportant << '\n';
}

static bool load_headers(const char* path, BitmapHeaders& bitmap_headers) {
    unsigned char bitmap_header_raw[HEADERS_SIZE]{};
    if (!load_raw_file_data(path, bitmap_header_raw, HEADERS_SIZE)) {
        cerr << "Can't open or read file: " << path << '\n';
        return false;
    }
    if (!check_signature(bitmap_header_raw)) {
        cerr << "Not a BMP file: " << path << '\n';
        return false;
    }
    map_header(bitmap_header_raw, bitmap_headers);
    print_bitmap_headers(bitmap_headers);
    return true;
}

static void print_pixel(const char* corner, const VPixel& p) {
    cout << corner << ": R:" << static_cast<int>(p.r)
          << " G:" << static_cast<int>(p.g)
          << " B:" << static_cast<int>(p.b) << '\n';
}

int main(const int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "image.bmp";

    BitmapHeaders bitmap_headers{};
    if (!load_headers(path, bitmap_headers)) return 1;

    if (bitmap_headers.bitmap_bits_per_pixel != 24 || bitmap_headers.bitmap_compression != 0) {
        cerr << "Only uncompressed 24-bit BMP is supported\n";
        return 1;
    }

    const int width = bitmap_headers.bitmap_width;
    const bool top_down = bitmap_headers.bitmap_height < 0;
    const int height = top_down ? -bitmap_headers.bitmap_height : bitmap_headers.bitmap_height;
    if (width <= 0 || height <= 0) {
        cerr << "Invalid image size\n";
        return 1;
    }

    const int row_size = (width * 3 + 3) / 4 * 4;
    const int data_size = row_size * height;

    const auto pixels_raw = new unsigned char[data_size];
    if (!load_raw_file_data(path, pixels_raw, data_size, bitmap_headers.bitmap_data_offset)) {
        cerr << "Can't read pixel data\n";
        delete[] pixels_raw;
        return 1;
    }

    auto get_pixel = [&](const int x, const int y) -> const VPixel& {
        const int row = top_down ? y : height - 1 - y;
        return *reinterpret_cast<const VPixel*>(pixels_raw + row * row_size + x * 3);
    };

    print_pixel("upper-left", get_pixel(0, 0));
    print_pixel("upper-right", get_pixel(width - 1, 0));
    print_pixel("bottom-left", get_pixel(0, height - 1));
    print_pixel("bottom-right", get_pixel(width - 1, height - 1));

    delete[] pixels_raw;
    return 0;
}
