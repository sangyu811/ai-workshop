import os

cwd = os.getcwd()
path = os.path.join(cwd, "index.html")
html = open(path, "r", encoding="utf-8").read()

# Replace the ENTIRE pay modal from opening to closing
old_modal = '''<div class="modal-overlay" id="payModal">
<div class="modal-box pay-modal" style="max-width:440px;padding:24px">
<button class="modal-close" onclick="closePayModal()">&times;</button>
<div style="text-align:center;margin-bottom:14px">
<h2 style="font-size:1.1rem;margin-bottom:3px">\u652f\u4ed8\u65b9\u5f0f</h2>
<p style="font-size:.85rem;color:#6e6e73;margin:0">\u5148\u51fa\u7a3f\uff0c\u786e\u8ba4\u6ee1\u610f\u540e\u518d\u4ed8\u6b3e</p>
</div>
<div class="pay-grid">
<div class="pay-card wx">
<span class="pay-badge wx">\u5fae\u4fe1\u652f\u4ed8</span>
<div class="qr-wrap"><img src="wechat-pay.png" alt="\u5fae\u4fe1\u652f\u4ed8"></div>
<div class="pay-name">\u5fae\u4fe1\u652f\u4ed8</div>
<div class="pay-hint">\u626b\u7801\u5373\u53ef\u4ed8\u6b3e</div>
</div>
<div class="pay-card ali">
<span class="pay-badge ali">\u652f\u4ed8\u5b9d</span>
<div class="qr-wrap"><img src="alipay.png" alt="\u652f\u4ed8\u5b9d"></div>
<div class="pay-name">\u652f\u4ed8\u5b9d</div>
<div class="pay-hint">\u626b\u7801\u5373\u53ef\u4ed8\u6b3e</div>
</div>
</div>
<div class="pay-divider">\u652f\u4ed8\u6d41\u7a0b</div>
<div class="pay-flow">
<span class="step active">\u2460 \u4e0b\u5355</span>
<span class="arrow">\u2192</span>
<span class="step">\u2461 \u51fa\u7a3f</span>
<span class="arrow">\u2192</span>
<span class="step">\u2462 \u786e\u8ba4</span>
<span class="arrow">\u2192</span>
<span class="step">\u2463 \u4ed8\u6b3e</span>
</div>
<div class="pay-footer">
\u652f\u6301\u5fae\u4fe1\u652f\u4ed8 / \u652f\u4ed8\u5b9d / \u8f6c\u8d26 &middot; <strong>\u5148\u51fa\u7a3f\u518d\u4ed8\u6b3e</strong>
</div>
</div>
</div>'''

new_modal = '''<div class="modal-overlay" id="payModal">
<div class="modal-box" style="max-width:380px;padding:28px 32px 24px">
<button class="modal-close" onclick="closePayModal()">&times;</button>
<div style="text-align:center">
<p style="font-size:.8rem;color:#6e6e73;margin:0 0 16px">\u5148\u51fa\u7a3f &middot; \u786e\u8ba4\u540e\u518d\u4ed8\u6b3e</p>
<img src="wechat-pay.png" alt="\u652f\u4ed8\u4e8c\u7ef4\u7801" style="width:130px;height:130px;border-radius:12px;display:block;margin:0 auto 14px;border:2px solid #f5f5f7">
<div style="display:flex;gap:6px;justify-content:center;margin-bottom:14px">
<span style="font-size:.65rem;font-weight:500;background:linear-gradient(135deg,#fa5151,#d63030);color:#fff;padding:2px 10px;border-radius:20px">\u5fae\u4fe1\u652f\u4ed8</span>
<span style="font-size:.65rem;font-weight:500;background:linear-gradient(135deg,#1677ff,#0d5bd6);color:#fff;padding:2px 10px;border-radius:20px">\u652f\u4ed8\u5b9d</span>
<span style="font-size:.65rem;font-weight:500;background:#f5f5f7;color:#6e6e73;padding:2px 10px;border-radius:20px">\u8f6c\u8d26</span>
</div>
<div class="pay-flow" style="margin-bottom:0">
<span class="step active">\u2460 \u4e0b\u5355</span>
<span class="arrow">\u2192</span>
<span class="step">\u2461 \u51fa\u7a3f</span>
<span class="arrow">\u2192</span>
<span class="step">\u2462 \u786e\u8ba4</span>
<span class="arrow">\u2192</span>
<span class="step">\u2463 \u4ed8\u6b3e</span>
</div>
</div>
</div>
</div>'''

if old_modal in html:
    html = html.replace(old_modal, new_modal)
    print("Modal replaced OK")
else:
    print("WARNING: Could not match old modal!")
    # Try to find it
    i = html.find('id="payModal"')
    if i >= 0:
        print(f"Found payModal at {i}, trying partial match...")
        # Find the opening and closing divs
        end_marker = html.find('</div>\n<div class="toast"', i)
        if end_marker > 0:
            print(f"Found end marker at {end_marker}")
            old_content = html[i:end_marker]
            # Replace only the content inside
            html = html[:i] + new_modal[new_modal.find('id="payModal"'):] + html[end_marker:]
            print("Partial replacement done")

# Remove old pay-modal CSS classes that are no longer used
for css_class in [".pay-modal", ".pay-grid", ".pay-card.wx", ".pay-card.ali", ".pay-badge.wx", ".pay-badge.ali",
                  ".pay-card .qr-wrap", ".pay-card .pay-name", ".pay-card .pay-hint",
                  ".pay-card.wx .qr-wrap", ".pay-card.ali .qr-wrap",
                  ".pay-card:hover", ".pay-card.wx:hover", ".pay-card.ali:hover",
                  ".pay-card::before", ".pay-divider", ".pay-card", ".pay-flow .step.active",
                  ".pay-card .qr-wrap img"]:
    start = html.find(css_class + "{")
    if start >= 0:
        end = html.find("}", start) + 1
        while html.find("{", start, end) >= 0:
            end = html.find("}", end) + 1
        html = html[:start] + html[end:]

open(path, "w", encoding="utf-8").write(html)
print(f"Updated. Size: {len(html)}")

# Verify
html2 = open(path, "r", encoding="utf-8").read()
checks = {
    "Single QR code (130px)": "width:130px;height:130px" in html2,
    "Modal exists": "payModal" in html2,
    "WeChat Pay badge": "\u5fae\u4fe1\u652f\u4ed8" in html2,
    "Alipay badge": "\u652f\u4ed8\u5b9d" in html2,
    "Transfer badge": "\u8f6c\u8d26" in html2,
    "Flow steps preserved": "\u2460 \u4e0b\u5355" in html2,
    "No dual cards (pay-grid)": "pay-grid" not in html2,
    "No pay-card classes": "pay-card" not in html2 or "pay-card" in html2 and "pay-card{" not in html2,
    "QR image": "wechat-pay.png" in html2,
    "open/close functions": "openPayModal" in html2,
    "Old pay-modal CSS gone": ".pay-modal" not in html2 or ".pay-modal{" not in html2,
}
print("\n=== Verification ===")
ok = sum(1 for v in checks.values() if v)
for k, v in checks.items():
    print(f"  [{'OK' if v else 'FAIL'}] {k}")
print(f"\nPassed: {ok}/{len(checks)}")
