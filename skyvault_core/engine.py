
from flask import Blueprint
from apscheduler.schedulers.background import BackgroundScheduler
import time, random

roi_engine = Blueprint('roi_engine', __name__)

# Simulated ROI tracker (placeholder logic)
profit = 0.0
vault_thresholds = [50000, 250000, 5000000, 25000000, 100000000, 250000000, 1000000000]
current_threshold_index = 0

def simulate_roi_cycle():
    global profit, current_threshold_index
    new_earning = random.uniform(500, 1500)
    profit += new_earning
    print(f"[SkyVault ROI Engine] +${new_earning:,.2f} | Total: ${profit:,.2f}")

    if current_threshold_index < len(vault_thresholds) and profit >= vault_thresholds[current_threshold_index]:
        threshold_hit = vault_thresholds[current_threshold_index]
        print(f"\n🚀 THRESHOLD REACHED: ${threshold_hit:,.0f} — Triggering vault logic!\n")
        current_threshold_index += 1

scheduler = BackgroundScheduler()
scheduler.add_job(simulate_roi_cycle, 'interval', seconds=15)
scheduler.start()

@roi_engine.route('/vault-status')
def vault_status():
    return {
        "profit": f"${profit:,.2f}",
        "next_threshold": f"${vault_thresholds[current_threshold_index]:,.0f}" if current_threshold_index < len(vault_thresholds) else "MAXED",
        "status": "🔁 Active",
    }
