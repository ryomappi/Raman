import sys
from RamanSpectrumClass import RamanSpectrum


def run(img_path, spectrum_output_name, csv_path=None, processed_output_name=None) -> None:
    raman_spectrum = RamanSpectrum(img_path)
    print("Successfully read the image")
    raman_spectrum.get_spectrum(spectrum_output_name)
    print("Successfully saved the spectrum graph")
    raman_spectrum.save_raw_spectrum(spectrum_output_name)
    print("Successfully saved the raw spectrum data")
    if csv_path is not None and processed_output_name is not None:
        raman_spectrum.outFigCSV(csv_path, processed_output_name)
        print("Successfully saved the processed spectrum data and graph")

if __name__ == '__main__':
    args = sys.argv
    # 例外処理
    if len(args) != 3 and len(args) != 5:
        print("Usage: python src/raman.py <img_path> <spectrum_output_name> [<csv_path> <processed_output_name>]")
        sys.exit(1)
    
    # 実行
    if len(args) == 3:
        run(args[1], args[2])
    else:
        run(args[1], args[2], args[3], args[4])
