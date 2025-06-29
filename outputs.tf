output "api_gateway_url" {
  description = "Public URL to trigger the Lambda"
  value       = "${aws_apigatewayv2_api.api.api_endpoint}/run-script"
}
