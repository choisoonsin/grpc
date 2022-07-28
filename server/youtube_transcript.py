from youtube_transcript_api import YouTubeTranscriptApi

transcript_list = YouTubeTranscriptApi.list_transcripts("Dpp1sIL1m5Q")

print(transcript_list)

transcript = transcript_list.find_transcript(['en'])

print(dir(transcript))

print(transcript.video_id)
print(transcript.is_translatable)
print(transcript.fetch())
