import requests
import uuid
import datetime

def simulasi_biaya_impor(kode_barang, nilai_komoditas):
  """
  Simulasi biaya impor berdasarkan kode barang dan nilai komoditas.

  Args:
    kode_barang: Kode barang (8 karakter).
    nilai_komoditas: Nilai komoditas.

  Returns:
    Dictionary berisi data simulasi biaya impor.
  """

  # Ambil uraian barang dari API
  url_barang = f"https://insw-dev.ilcs.co.id/my/n/barang?hs_code={kode_barang}"
  response_barang = requests.get(url_barang)
  if response_barang.status_code == 200:
    uraian_barang = response_barang.json()["uraian"]
  else:
    raise Exception("Gagal mengambil data uraian barang")

  # Ambil tarif biaya impor dari API
  url_tarif = f"https://insw-dev.ilcs.co.id/my/n/tarif?hs_code={kode_barang}"
  response_tarif = requests.get(url_tarif)
  if response_tarif.status_code == 200:
    tarif_bm = response_tarif.json()["bm"]
  else:
    raise Exception("Gagal mengambil data tarif biaya impor")

  # Hitung nilai BM
  nilai_bm = nilai_komoditas * tarif_bm / 100

  # Buat data simulasi
  data_simulasi = {
    "id_simulasi": str(uuid.uuid4()),
    "kode_barang": kode_barang,
    "uraian_barang": uraian_barang,
    "bm": tarif_bm,
    "nilai_komoditas": nilai_komoditas,
    "nilai_bm": nilai_bm,
    "waktu_insert": datetime.datetime.now().isoformat()
  }

  return data_simulasi

# Contoh penggunaan
kode_barang = "10079000"
nilai_komoditas = 1000000

data_simulasi = simulasi_biaya_impor(kode_barang, nilai_komoditas)

print("Data Simulasi Biaya Impor:")
print(data_simulasi)
