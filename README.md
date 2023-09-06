# Spotify extract

## Requirements

To run the Cloud Function, you will need a Spotify Account to get the token:
```
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>"
```

## Deployement

To Deploy the Cloud Function and all the necessary, go into the terraform folder:
```
cd terraform
```

You will need to init and Apply:

```
terraform init
terraform apply
```

## Run

Once the services are deployed, you can run the Cloud Function with the following arguments:

```
{
    "token": "<token>",
    "spotify_id": "<spotify_id>"
}
```

The spotify_id is the ID of the artist you want to extract the tracks.
To get it, you can find it in the Spotify URL of the artist.