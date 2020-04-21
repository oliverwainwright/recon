#!/bin/bash

ACCOUNT_ID="281566"
YOUR_LICENSE_KEY="y6cEXm8uBtci7VKp"
    
# ASN
# Database URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-ASN&license_key=${YOUR_LICENSE_KEY}&suffix=tar.gz

# SHA256 URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-ASN&license_key=${YOUR_LICENSE_KEY}&suffix=tar.gz.sha256

# ASN CSV
# Database URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-ASN-CSV&license_key=${YOUR_LICENSE_KEY}&suffix=zip

# SHA256 URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-ASN-CSV&license_key=${YOUR_LICENSE_KEY}&suffix=zip.sha256

# City
# Database URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=${YOUR_LICENSE_KEY}&suffix=tar.gz

# SHA256 URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=${YOUR_LICENSE_KEY}&suffix=tar.gz.sha256

# City CSV
# Database URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City-CSV&license_key=${YOUR_LICENSE_KEY}&suffix=zip

# SHA256 URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City-CSV&license_key=${YOUR_LICENSE_KEY}&suffix=zip.sha256

# Country
# Database URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country&license_key=${YOUR_LICENSE_KEY}&suffix=tar.gz

# SHA256 URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country&license_key=${YOUR_LICENSE_KEY}&suffix=tar.gz.sha256

# Country CSV
# Database URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country-CSV&license_key=${YOUR_LICENSE_KEY}&suffix=zip

# SHA256 URL
wget https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country-CSV&license_key=${YOUR_LICENSE_KEY}&suffix=zip.sha256
