import random

def analyze_rumination(cow_id):
    rumination_minutes = random.randint(10, 120)

    if rumination_minutes < 30:
        return {
            "cow_id": cow_id,
            "status": "ALERT",
            "message": "Cow is not chewing properly. Possible heat or health issue."
        }
    else:
        return {
            "cow_id": cow_id,
            "status": "NORMAL",
            "message": "Cow behavior is normal."
        }

def process_video(video_path):
    print(f"Processing video: {video_path}")
    
    # simulated processing
    result = analyze_rumination(7)
    
    return result


if __name__ == "__main__":
    output = process_video("sample_cow_video.mp4")
    print(output)