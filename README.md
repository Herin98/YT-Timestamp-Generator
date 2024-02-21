#Project Description:

This project, "YouTube Timestamp Generator", is a web application that helps users automatically generate timestamps for YouTube videos. Users simply need to provide the URL of a YouTube video, and the app will fetch the transcript, analyze it, and generate concise timestamps representing key topics or ideas in the video.

##Key Features:

- Automatic timestamp generation: Uses a large language model (LLM) to analyze video transcripts and identify relevant segments for timestamps.
- Easy-to-use interface: Simple web interface with a single input field for the video URL.
- Clear and concise timestamps: Generated timestamps are presented in a simple format with titles reflecting the content of each segment.
- Copy functionality: Allows users to easily copy the generated timestamps to the clipboard.

##Requirements:

- Python 3.6+
- Flask
- YouTube Transcript API
- Langchain Core
- Langchain Google GenAI
- dotenv

##Installation:

1. Clone this repository: git clone https://github.com/your-username/youtube-timestamp-generator.git
2. Navigate to the project directory: cd youtube-timestamp-generator
3. Install dependencies: pip install -r requirements.txt
4. Create a .env file in the project directory and add your Google API key: GOOGLE_API_KEY=your_api_key
5. Running the application:
  1) Start the development server: flask run
  2) Access the application in your web browser: http://localhost:5000

##Contribution:

We welcome contributions to this project! Feel free to fork the repository and submit pull requests with your improvements. 
Some of the contributing direction I have mentioned below. Feel free to work on those or something you found ;) 
####Simple contribution: 
- LLM is not accepting harmful or explicit content(for ex. Right now - Acon, was not accepted). Generate Timestamps for those type content.
####Medium contribution:
- Error Handling: Ensure robust error handling throughout the code, especially when dealing with external APIs like YouTube Transcript API and generative AI from Google. Handle potential errors gracefully and provide meaningful error messages to the user.
- Optimization: Depending on the size of the transcript, the generation of timestamps might take some time. Consider optimizing the process or providing feedback to the user while the timestamps are being generated, such as a loading spinner or progress bar.
- User Interface: Enhance the user interface to provide better feedback and user experience.

##Additional Notes:

- The accuracy of the generated timestamps may vary depending on the video content and the capabilities of the LLM.
- This project is still under development.

##Screenshots
- Thunder Imagine Dragons: https://youtu.be/fKopy74weus?feature=shared
![ytGen3](https://github.com/Herin98/YT-Timestamp-Generator/assets/142152236/733d618f-e965-4c23-9b7b-71bf53abe742)

- NeetCode video : https://youtu.be/UrcwDOEBzZE?feature=shared
![ytGen1](https://github.com/Herin98/YT-Timestamp-Generator/assets/142152236/cd7be642-81ff-43fc-b82a-53b36efa6027)

- Night Changes : https://youtu.be/syFZfO_wfMQ?feature=shared
![ytGen2](https://github.com/Herin98/YT-Timestamp-Generator/assets/142152236/91db753e-89ce-43e1-95a4-fa3d2a061ac3)
