variable "gcp_credentials" {
  type    = string
  default = "../inspired-carver-396617-0257c37f86c7.json"
}

variable "project_id" {
  type    = string
  default = "inspired-carver-396617"
}

variable "region" {
  type    = string
  default = "europe-central2"
}

variable "artifact_registry_hostname" {
  type    = string
  default = "europe-central2-docker.pkg.dev"
}

variable "artifact_registry_name" {
  type    = string
  default = "code-to-image-generator"
}

variable "docker_image_name" {
  type    = string
  default = "code-to-image-generator"
}

variable "docker_image_tag" {
  type    = string
  default = "vc35ef43d3a3c783ab0095a3d046deba291382c07"
}


