import discord
import requests
from io import BytesIO
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.applications.resnet50 import ResNet50
import numpy as np
from PIL import Image
import re

# Load the pre-trained model
model = ResNet50(weights='imagenet')



def catanddog(message,imagenet):
    image_url = None

    # Extract image URL from the message content using regex
    url_match = re.search(r"(?P<url>https?://[^\s]+)", imagenet)
    if url_match:
        image_url = url_match.group("url")

    if image_url:
        try:
            # Download the image from the URL using requests
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            image = image.resize((224, 224))  # Resize to match the model input size
            image_array = preprocess_input(np.array(image))
            image_array = np.expand_dims(image_array, axis=0)

            # Make predictions
            predictions = model.predict(image_array)
            decoded_predictions = decode_predictions(predictions, top=1)[0]
            top_prediction = decoded_predictions[0]

            if 'dog' in top_prediction[1]:
                result = 'It looks like a dog!'
            elif 'cat' in top_prediction[1]:
                result = 'It looks like a cat!'
            else:
                result = 'I cannot identify the animal.'

            # Create and send an embedded message
            embed = discord.Embed(title="Image Identification Result", description=result, color=0xF9D342)
            embed.set_image(url=image_url)
            return embed

        except Exception as e:
            # Handle any exceptions that may occur during image processing
            error_message = f"Error occurred: {e}"
            return error_message



# Test cases

result1 = catanddog(
    "!!idanimal https://cdn.discordapp.com/attachments/831409359572697169/1131634961536004177/projectcat.jpeg",
    "https://cdn.discordapp.com/attachments/831409359572697169/1131634961536004177/projectcat.jpeg"
)
print(result1)
