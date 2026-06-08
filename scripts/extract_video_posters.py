"""
Extract JPEG poster frames from MP4 files in docs/media/.

Usage (from project root):
    pip install opencv-python-headless
    python scripts/extract_video_posters.py

Output: docs/media/<video-basename>-poster.jpg next to each .mp4
"""
from __future__ import annotations

import argparse
import os
import sys

try:
    import cv2
except ImportError:
    print("Install OpenCV first: pip install opencv-python-headless", file=sys.stderr)
    raise SystemExit(1)


def extract_poster(video_path: str, poster_path: str, time_ms: int = 1000, max_width: int = 1280) -> None:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise OSError(f"Cannot open video: {video_path}")

    cap.set(cv2.CAP_PROP_POS_MSEC, time_ms)
    ok, frame = cap.read()
    if not ok:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ok, frame = cap.read()
    cap.release()

    if not ok or frame is None:
        raise OSError(f"Cannot read frame from: {video_path}")

    height, width = frame.shape[:2]
    if width > max_width:
        scale = max_width / width
        frame = cv2.resize(frame, (max_width, int(height * scale)), interpolation=cv2.INTER_AREA)

    os.makedirs(os.path.dirname(poster_path) or ".", exist_ok=True)
    cv2.imwrite(poster_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 85])


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract poster JPGs from docs/media MP4 files.")
    parser.add_argument(
        "--media-dir",
        default=os.path.join("docs", "media"),
        help="Directory containing MP4 files (default: docs/media)",
    )
    parser.add_argument(
        "--time-ms",
        type=int,
        default=1000,
        help="Timestamp for the poster frame (default: 1000 ms)",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.media_dir):
        raise SystemExit(f"Media directory not found: {args.media_dir}")

    mp4_files = sorted(f for f in os.listdir(args.media_dir) if f.lower().endswith(".mp4"))
    if not mp4_files:
        print(f"No MP4 files in {args.media_dir}")
        return

    for name in mp4_files:
        base, _ = os.path.splitext(name)
        video_path = os.path.join(args.media_dir, name)
        poster_path = os.path.join(args.media_dir, f"{base}-poster.jpg")
        extract_poster(video_path, poster_path, time_ms=args.time_ms)
        size_kb = os.path.getsize(poster_path) // 1024
        print(f"[OK] {poster_path} ({size_kb} KB)")


if __name__ == "__main__":
    main()
