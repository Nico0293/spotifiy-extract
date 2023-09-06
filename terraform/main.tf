provider "google" {
  project     = "certiftest"
  region      = "northamerica-northeast1"
}

resource "google_storage_bucket" "output_bucket" {
  name = "testnf_20230901"
  location = "US"
}

resource "google_storage_bucket" "code_bucket" {
  name = "code_bucket_20230906"
  location = "US"
}

resource "google_storage_bucket_object" "archive" {
  name   = "code.zip"
  bucket = google_storage_bucket.code_bucket.name
  source = "../zip/code.zip"
}

resource "google_cloudfunctions_function" "function" {
  name        = "spotify-extract"
  description = "Extract all the tracks of each album based on the spotify_id's author provided"
  runtime     = "python310"

  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket.code_bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  trigger_http          = true
  entry_point           = "hello_http"
}