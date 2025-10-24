#!/usr/bin/env python3
"""
Simple command-line QR Code generator.

Usage:
  python main.py --url <URL> [--output-dir qr_codes] [--file-name name.png]

The script reads configuration from environment variables as well:
  QR_URL (overridden by --url)
  QR_OUTPUT_DIR
  QR_FILE_NAME

It depends on qrcode and pillow.
"""
import os
import argparse
from pathlib import Path
import qrcode


def generate_qr(url: str, output_dir: Path, file_name: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    img = qrcode.make(url)
    out_path = output_dir / file_name
    img.save(out_path)
    return out_path


def parse_args():
    parser = argparse.ArgumentParser(description="Generate a QR code image for a URL")
    parser.add_argument("--url", required=False, help="URL to encode into the QR code")
    parser.add_argument("--output-dir", default=None, help="Directory to write QR code images")
    parser.add_argument("--file-name", default=None, help="Output file name (e.g. code.png)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Environment variable defaults
    env_url = os.getenv("QR_URL")
    env_output_dir = os.getenv("QR_OUTPUT_DIR", "qr_codes")
    env_file_name = os.getenv("QR_FILE_NAME", "qrcode.png")

    url = args.url or env_url
    if not url:
        print("Error: no URL provided. Use --url or set QR_URL environment variable.")
        raise SystemExit(2)

    output_dir = Path(args.output_dir or env_output_dir)
    file_name = args.file_name or env_file_name

    out_path = generate_qr(url, output_dir, file_name)
    print(f"QR code written to: {out_path}")


if __name__ == "__main__":
    main()
