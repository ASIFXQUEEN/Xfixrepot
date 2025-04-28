import sys
import json
import asyncio
from pyrogram import Client
from pyrogram.raw.functions.account import ReportPeer
from pyrogram.raw.types import *

def get_reason(text):
    reason_map = {
        "Report for child abuse": InputReportReasonChildAbuse(),
        "Report for impersonation": InputReportReasonFake(),
        "Report for copyrighted content": InputReportReasonCopyright(),
        "Report an irrelevant geogroup": InputReportReasonGeoIrrelevant(),
        "Reason for Pornography": InputReportReasonPornography(),
        "Report an illegal drug": InputReportReasonIllegalDrugs(),
        "Report for offensive person detail": InputReportReasonPersonalDetails(),
        "Report for spam": InputReportReasonSpam(),
        "Report for Violence": InputReportReasonViolence()
    }
    return reason_map.get(text, InputReportReasonOther())

async def main(message):
    try:
        config = json.load(open("config.json"))
        if not all(k in config for k in ["Target", "accounts"]):
            raise ValueError("Invalid config structure")
    except Exception as e:
        print(f"Config Error: {str(e)}")
        return

    resportreason = get_reason(message)
    target = config['Target']
    
    for account in config["accounts"]:
        async with Client(
            name="Session",
            session_string=account["Session_String"]
        ) as app:
            try:
                peer = await app.resolve_peer(target)
                if isinstance(peer, (InputPeerChannel, InputPeerChat, InputPeerUser)):
                    report_peer = ReportPeer(
                        peer=peer,
                        reason=resportreason,
                        message=message
                    )
                    result = await app.invoke(report_peer)
                    print(f"✅ Reported by {account['OwnerName']} | Result: {result}")
                else:
                    print("❌ Unsupported peer type")
            except Exception as e:
                print(f"❌ Failed {account['OwnerName']}: {str(e)}")

async def run():
    if len(sys.argv) != 2:
        print("Usage: python report.py 'Report Reason'")
        return
    await main(sys.argv[1])

if __name__ == "__main__":
    asyncio.run(run())
