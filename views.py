import os

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def get_nasa_data(request):
    api_url = "https://data.gesdisc.earthdata.nasa.gov/data/TRMM_RT/TRMM_3B42RT.7/2017/365/3B42RT.2018010100.7.nc4"
    token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImFncmlkYXRhZHluYW1vIiwiZXhwIjoxNzMyODk2MTIyLCJpYXQiOjE3Mjc3MTIxMjIsImlzcyI6Imh0dHBzOi8vdXJzLmVhcnRoZGF0YS5uYXNhLmdvdiJ9.enJ-MkaMQADlTOHmrDxXZBFrDAxhVRcd8zqk5lKPNZx7-k-dXXqWbmwDmdpk9Lmag5ovYewIMhwDshwRnrf-sS0iZ9JOE_YXmubQrxWRym8qvnE2aaYfWBwqlnZPX0VZTwBPtEW_iY0wyYQC9S9Vh8eUEPBzfARcKAOcv_MhDjNAdEz-UGjmipSblSOS7bnxlsPMi9qYnlrXQ8uF5M1gfs9oM0AGDmJ0BC1EfOqMgoRzi6WebkRk8PPIp8fPkqSwcS4Ctd3rI2JN9ENhFUeIORqZ_zQlMcPmouNd1lTMsOxKg9eEoBuToAJ4w8Z8oezuZP-fMnS_Y_X-UnDUsKmtAA"  # Replace with your actual JWT token
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/octet-stream"  # Set this to handle binary data
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Save the .nc4 file to a designated folder
        file_path = os.path.join(os.path.dirname(__file__), 'static', 'nasa_data.nc4')
        with open(file_path, 'wb') as file:  # Open in binary write mode
            file.write(response.content)

        return JsonResponse({"message": "Data fetched successfully!", "download_ready": True})

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Failed to fetch data: {str(e)}"})

def download_nasa_data(request):
    file_path = os.path.join(os.path.dirname(__file__), 'static', 'nasa_data.nc4')

    # Check if the file exists before attempting to download it
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:  # Open in binary read mode
            response = HttpResponse(file.read(), content_type='application/netcdf')
            response['Content-Disposition'] = 'attachment; filename="nasa_data.nc4"'
            return response
    else:
        return HttpResponse("File not found.", status=404)

def home(request):
    return render(request, 'home.html')
