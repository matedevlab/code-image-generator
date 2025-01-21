terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.9"
    }
  }

  required_version = ">= 1.2.0"
}

provider "google" {
  credentials = file(var.gcp_credentials)
  project     = var.project_id
  region      = var.region
}
