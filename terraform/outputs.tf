output "vm_public_ip" {
  description = "Public IP address of the Nginx VM"
  value       = google_compute_instance.nginx_vm.network_interface[0].access_config[0].nat_ip
}
