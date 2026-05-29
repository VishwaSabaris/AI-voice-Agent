from stt.fast_listen import listen
from slm.slm_engine import predict
from tts.tts_engine import speak
from utils.email_sender import send_email


def is_yes(reply):

    yes_words = [
        "ஆம்",
        "ஆமா",
        "yes",
        "ok",
        "okay",
        "சரி",
        "correct"
    ]

    reply = reply.lower()

    return any(word in reply for word in yes_words)


def main():

    print("\n🚀 AI Restaurant Agent Started...\n")

    speak("வணக்கம்! என்ன ஆர்டர் செய்ய விரும்புகிறீர்கள்?")

    while True:

        try:
            # Listen to customer
            customer_text = listen()

            if not customer_text:
                speak("மீண்டும் சொல்லுங்கள்")
                continue

            print(f"\n📝 Customer said: {customer_text}")

            # Extract order
            order = predict(customer_text)

            print("\n📦 Extracted Order:")
            print(order)

            confirm_text = (
                f"நீங்கள் {order['area']} பகுதியில் "
                f"{order['quantity']} {order['item']} "
                f"ஆர்டர் செய்துள்ளீர்களா? "
                f"சரி என்றால் ஆம் சொல்லுங்கள்."
            )

            speak(confirm_text)

            # Listen for confirmation
            confirmation = listen()

            print(f"📝 Customer confirmation: {confirmation}")

            if is_yes(confirmation):

                speak("சரி. உங்கள் order confirmed.")

                print("\n✅ Order Confirmed")

                try:
                    send_email(order)
                    print("📧 Email Sent")
                except Exception as e:
                    print("Email Error:", e)

                speak("நன்றி. உங்கள் ஆர்டர் பதிவு செய்யப்பட்டது.")

                break

            else:
                speak("சரி. உங்கள் order மீண்டும் சொல்லுங்கள்.")

        except KeyboardInterrupt:
            print("\n🛑 Agent stopped")
            break

        except Exception as e:
            print("❌ Error:", e)
            speak("சில தொழில்நுட்ப பிரச்சனை ஏற்பட்டுள்ளது")


if __name__ == "__main__":
    main()
