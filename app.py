from flask import Flask, render_template, request
from dotenv import find_dotenv, load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import os
import re
import google.generativeai as genai

client = genai.configure(api_key="AIzaSyCHdM5I2L9EIwKNssBLaf6occrADIsfCh4")
client = genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
#genai.configure(api_key="AIzaSyCHdM5I2L9EIwKNssBLaf6occrADIsfCh4")

load_dotenv(find_dotenv())

llm_model = 'gemini-pro'

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["videoUrl"]
        video_id = extract_video_id(video_url)
        try:
            transcript = fetch_transcript(video_id)
            timestamps = generate_timestamps(transcript)
            return render_template("index.html", timestamps=timestamps)
        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html", timestamps=None)


def extract_video_id(url):
    """
    Extracts the YouTube video ID from the URL.
    """
    # Regular expression for extracting the video ID
    regex = r"(youtu\.be\/|youtube\.com\/(?:watch\?v=|v\/|embed\/|watch\?.+&v=))((\w|-){11})"
    matches = re.search(regex, url)
    if matches:
        return matches.group(2)
    raise ValueError("Invalid YouTube URL")

def fetch_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id)
    # format transcript

    formatted_transcript = format_timestamps(transcript)
    print(f"FORMATTED::: {formatted_transcript}")
    return formatted_transcript

def format_timestamps(json_data):
    formatted_timestamps = []

    for entry in json_data:
        text = entry.get("text", "")

        # Check if 'text' starts with '['
        if text.startswith("["):
            # Skip this entry
            continue

        # Convert 'start' from seconds to 'minutes:seconds' format
        minutes = int(entry["start"] // 60)
        seconds = int(entry["start"] % 60)
        formatted_time = f"{minutes:02}:{seconds:02}"

        # Combine formatted time with 'text'
        formatted_entry = f"{formatted_time} || {text}"
        formatted_timestamps.append(formatted_entry)

        # Join all formatted timestamps into a single string separated by newlines
    return "\n".join(formatted_timestamps)

def generate_timestamps(transcript):
    # Todo: maybe use langchain to make sure that in cases when the transcript's tokens exceed the
    # limit, we can bypass the token limit issues!!! )
    template = f"""
            As an AI skilled in analyzing YouTube video content, your task is to create up to 6 accurate timestamps from the provided transcript. Each timestamp should represent a distinct topic or main idea in the video.

            Guidelines for Timestamp Generation:
            1. Analyze the transcript without summarizing it.
            2. Ensure timestamps are well-spaced, each representing a complete topic or idea.
            3. Limit the total number of timestamps to 6.
            4. Titles for timestamps must be concise and clearly reflect the content of the segment.

            Timestamp Format:
            00:00 || [Title for the first segment]
            02:56 || [Title for the next segment]
            ... and so on.

            Based on the guidelines, generate the timestamps from this transcript:

            {transcript}
       
        """

    response = client.chat.completions.create(
        model=llm_model,
        messages=[
            {
                "role": "system",
                "content": "You are a very knowledgeable Programmer and Youtuber",
            },
            {
                "role": "user",
                "content": f"{template}",
            },
        ],
        temperature=0.0
        # max_tokens=150,
    )
    print(response.choices[0].message.content4)
    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True, port=5000)
