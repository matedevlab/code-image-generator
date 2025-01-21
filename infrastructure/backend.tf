# Store terraform state in GCS
terraform {
  backend "gcs" {
    bucket = "code-to-image-generator"
    prefix = "terraform/state"
  }
}
