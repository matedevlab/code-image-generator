resource "google_app_engine_flexible_app_version" "myapp_on_app_engine" {
  version_id     = "v1"
  service        = "default"
  runtime        = "custom"
  serving_status = "SERVING"

  automatic_scaling {
    cool_down_period        = "120s"
    max_concurrent_requests = 10
    min_idle_instances      = 0
    min_total_instances     = 1
    max_total_instances     = 1
    cpu_utilization {
      target_utilization = 0.5
    }
  }

  liveness_check {
    path              = "/"
    check_interval    = "30s"
    timeout           = "4s"
    failure_threshold = 2
    success_threshold = 2
  }

  readiness_check {
    path              = "/"
    check_interval    = "5s"
    timeout           = "4s"
    app_start_timeout = "300s"
  }

  deployment {
    container {
      image = "${var.artifact_registry_hostname}/${var.project_id}/${var.artifact_registry_name}/${var.docker_image_name}:${var.docker_image_tag}"
    }
  }
}
