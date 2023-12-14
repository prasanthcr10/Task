import ssl
import socket
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    try:
        # Create a socket connection to the specified host and port
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the SSL certificate details
                cert = ssock.getpeercert()

                # Extract relevant information
                common_name = cert['subject'][0][0][1]
                expiration_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')

                # Check if the certificate is expired
                if expiration_date < datetime.now():
                    print(f"SSL certificate for {hostname} has expired.")
                else:
                    print(f"SSL certificate for {hostname} is valid until {expiration_date}.")
                print(f"Common Name: {common_name}")

    except Exception as e:
        print(f"Error checking SSL certificate: {str(e)}")

if __name__ == "__main__":
    website_url = "loco.gg"  # Replace with the URL of the website you want to check
    check_ssl_certificate(website_url)
