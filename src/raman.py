import sys
from RamanSpectrumClass import RamanSpectrum


def run(img_path, spectrum_output_name, csv_path, processed_output_name) -> None:
    raman_spectrum = RamanSpectrum(img_path)
    raman_spectrum.get_spectrum(spectrum_output_name)
    raman_spectrum.save_raw_spectrum(spectrum_output_name)
    raman_spectrum.outFigCSV(csv_path, processed_output_name)

if __name__ == '__main__':
    args = sys.argv
    # 実行
    run(args[1], args[2], args[3], args[4])
