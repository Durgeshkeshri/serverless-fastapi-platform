provider "google" {
  project     = var.project_id
  region      = var.region
  zone        = var.zone
  credentials = file("${path.module}/gcp-key.json")
}

resource "google_compute_instance" "nginx_vm" {
  name         = "nginx-vm"
  machine_type = "e2-micro"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"

    access_config {
      # Ephemeral public IP
    }
  }

  tags = ["nginx-server"]
}
