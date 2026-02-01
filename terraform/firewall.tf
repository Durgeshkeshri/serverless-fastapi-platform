resource "google_compute_firewall" "allow_http" {
  name    = "allow-http-nginx"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["nginx-server"]
}
