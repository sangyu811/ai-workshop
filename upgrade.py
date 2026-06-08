import re

html = open("C:\\Users\\25495\\Desktop\\新建文件夹\\startup-kit\\index.html", "r", encoding="utf-8").read()

# ====== NEW CSS ======
new_css = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:#f5f5f7;color:#1d1d1f;line-height:1.6}
.container{max-width:960px;margin:0 auto;padding:0 20px}
.hero{background:linear-gradient(135deg,#1d1d1f,#2d2d2f);color:#fff;padding:80px 0 60px;text-align:center}
.hero h1{font-size:2.8rem;font-weight:700;margin-bottom:12px}
.hero p{font-size:1.15rem;color:#a1a1a6;max-width:600px;margin:0 auto 28px}
.hero .badge{display:inline-block;background:#0071e3;color:#fff;padding:6px 16px;border-radius:20px;font-size:.85rem;font-weight:500;margin-bottom:20px}
.cta-btn{display:inline-block;background:#0071e3;color:#fff;padding:14px 36px;border-radius:30px;font-size:1.05rem;font-weight:600;text-decoration:none;border:none;cursor:pointer}
.cta-btn:hover{background:#0077ed}
.cta-btn.secondary{background:transparent;border:1.5px solid rgba(255,255,255,.4);margin-left:12px}
.section{padding:60px 0}
.section-title{font-size:1.8rem;font-weight:700;text-align:center;margin-bottom:40px}
.services-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:20px}
.service-card{background:#fff;border-radius:16px;padding:28px;box-shadow:0 2px 8px rgba(0,0,0,.04);transition:all .2s}
.service-card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,.08)}
.service-card .icon{font-size:2rem;margin-bottom:12px}
.service-card h3{font-size:1.15rem;font-weight:600;margin-bottom:8px}
.service-card p{font-size:.92rem;color:#6e6e73;margin-bottom:4px}
.service-card .price{font-weight:700;color:#0071e3;font-size:1.2rem}
.service-card .price small{font-size:.75rem;color:#6e6e73;font-weight:400}
.package-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-bottom:36px}
.package-card{background:#fff;border-radius:16px;padding:28px;box-shadow:0 2px 8px rgba(0,0,0,.04);text-align:center;position:relative;transition:all .2s;border:2px solid transparent}
.package-card:hover{box-shadow:0 8px 24px rgba(0,0,0,.08)}
.package-card.popular{border-color:#0071e3}
.package-card .pop-tag{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:#0071e3;color:#fff;padding:4px 16px;border-radius:20px;font-size:.75rem;font-weight:600}
.package-card h3{font-size:1.1rem;font-weight:600;margin-bottom:8px}
.package-card .big-price{font-size:2.4rem;font-weight:700;color:#1d1d1f;margin:8px 0}
.package-card .big-price small{font-size:.9rem;font-weight:400;color:#6e6e73}
.package-card .per-unit{font-size:.85rem;color:#34c759;font-weight:600;margin-bottom:12px}
.package-card ul{text-align:left;list-style:none;padding:0;margin:0 0 16px}
.package-card ul li{padding:4px 0;font-size:.88rem;color:#6e6e73}
.package-card ul li:before{content:"\\2713";color:#34c759;margin-right:8px;font-weight:700}
.pricing-table{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.04)}
.pricing-table table{width:100%;border-collapse:collapse}
.pricing-table th{background:#f5f5f7;padding:14px 20px;text-align:left;font-weight:600;font-size:.9rem;color:#6e6e73}
.pricing-table td{padding:14px 20px;border-bottom:1px solid #eee;font-size:.95rem}
.pricing-table tr:last-child td{border-bottom:none}
.pricing-table tr:hover{background:#fafafa}
.pricing-table .price-cell{font-weight:700;color:#1d1d1f;font-size:1.05rem}
.pricing-table .old-price{text-decoration:line-through;color:#c7c7cc;font-weight:400;font-size:.82rem;margin-right:6px}
.pricing-table .tag{display:inline-block;padding:2px 10px;border-radius:12px;font-size:.75rem;font-weight:500;margin-left:6px}
.pricing-table .tag.hot{background:#ff3b30;color:#fff}
.pricing-table .tag.pop{background:#e8f5e9;color:#2e7d32}
.pricing-table .tag.new{background:#e3f2fd;color:#1565c0}
.pricing-table .order-cell{text-align:center}
.pricing-table .mini-order-btn{padding:6px 16px;border:1px solid #0071e3;border-radius:8px;background:transparent;color:#0071e3;font-size:.8rem;font-weight:600;cursor:pointer;transition:all .2s}
.pricing-table .mini-order-btn:hover{background:#0071e3;color:#fff}
.why-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px}
.why-item{text-align:center;padding:20px}
.why-item .num{font-size:2.2rem;font-weight:700;color:#0071e3;margin-bottom:4px}
.why-item p{font-size:.92rem;color:#6e6e73}
.faq-item{background:#fff;border-radius:12px;padding:20px 24px;margin-bottom:10px;box-shadow:0 1px 4px rgba(0,0,0,.04)}
.faq-item q{font-weight:600;display:block;margin-bottom:6px}
.faq-item a{color:#6e6e73;font-size:.92rem}
.footer{text-align:center;padding:40px 0;color:#6e6e73;font-size:.85rem;border-top:1px solid #d2d2d7;margin-top:20px}
.modal-overlay{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.5);z-index:1000;align-items:center;justify-content:center}
.modal-overlay.show{display:flex}
.modal-box{background:#fff;border-radius:20px;padding:36px;width:90%;max-width:500px;max-height:90vh;overflow-y:auto;position:relative}
.modal-box h2{font-size:1.3rem;margin-bottom:6px}
.modal-box .modal-sub{color:#6e6e73;font-size:.9rem;margin-bottom:20px}
.modal-close{position:absolute;top:16px;right:20px;font-size:1.4rem;cursor:pointer;color:#c7c7cc;background:none;border:none;line-height:1}
.modal-close:hover{color:#1d1d1f}
.form-row{margin-bottom:14px}
.form-row label{display:block;font-weight:600;font-size:.85rem;margin-bottom:4px;color:#1d1d1f}
.form-row input,.form-row select,.form-row textarea{width:100%;padding:11px 14px;border:1.5px solid #d2d2d7;border-radius:10px;font-size:.92rem;font-family:inherit;transition:border .2s}
.form-row input:focus,.form-row select:focus,.form-row textarea:focus{outline:none;border-color:#0071e3}
.form-row textarea{resize:vertical;min-height:70px}
.total-bar{background:#f5f5f7;border-radius:12px;padding:14px 18px;display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.total-bar .total-label{font-size:.9rem;color:#6e6e73}
.total-bar .total-amount{font-size:1.4rem;font-weight:700;color:#1d1d1f}
.total-bar .total-amount small{font-size:.85rem;font-weight:400;color:#6e6e73}
.submit-btn{width:100%;padding:14px;background:#0071e3;color:#fff;border:none;border-radius:12px;font-size:1rem;font-weight:600;cursor:pointer;transition:background .2s}
.submit-btn:hover{background:#0077ed}
.submit-btn .sub{font-weight:400;font-size:.8rem;opacity:.7}
.float-order{position:fixed;bottom:24px;right:24px;z-index:999;background:#0071e3;color:#fff;width:56px;height:56px;border-radius:50%;border:none;font-size:1.6rem;cursor:pointer;box-shadow:0 4px 16px rgba(0,113,227,.4);transition:all .2s}
.float-order:hover{transform:scale(1.08);box-shadow:0 6px 24px rgba(0,113,227,.5)}
.float-label{display:none;position:absolute;right:64px;top:50%;transform:translateY(-50%);background:#1d1d1f;color:#fff;padding:6px 14px;border-radius:8px;font-size:.8rem;white-space:nowrap}
.float-order:hover .float-label{display:block}
@media(max-width:640px){
.hero h1{font-size:1.8rem}
.cta-btn.secondary{margin-left:0;margin-top:10px;display:block}
.package-grid{grid-template-columns:1fr}
.modal-box{padding:24px;border-radius:16px}
.float-order{bottom:16px;right:16px;width:50px;height:50px;font-size:1.4rem}
}"""

# Replace CSS
css_start = html.find("<style>")
css_end = html.find("</style>") + 8
html = html[:css_start] + "<style>" + new_css + html[css_end:]

# ====== NEW PRICING SECTION ======
new_pricing = """<div class="section" style="background:#f5f5f7" id="pricing"><div class="container">
<h2 class="section-title">选套餐更划算</h2>
<div class="package-grid">
<div class="package-card">
<h3>单篇体验</h3>
<div class="big-price">29<small>起</small></div>
<div class="per-unit">按篇支付，灵活试用</div>
<ul>
<li>任选一项服务</li>
<li>2小时内交付</li>
<li>免费修改到满意</li>
<li>先出稿后付款</li>
</ul>
<button class="cta-btn" style="padding:10px 28px;font-size:.9rem" onclick="openOrder('小红书笔记',29)">立即下单</button>
</div>
<div class="package-card popular">
<div class="pop-tag">推荐</div>
<h3>5篇套餐</h3>
<div class="big-price">99<small>起</small></div>
<div class="per-unit">省约32% / 低至19.8/篇</div>
<ul>
<li>任选服务自由搭配</li>
<li>优先排单，1小时交付</li>
<li>送1次免费加急</li>
<li>专属需求对接</li>
</ul>
<button class="cta-btn" style="padding:10px 28px;font-size:.9rem" onclick="openOrder('5篇套餐',99)">立即抢购</button>
</div>
<div class="package-card">
<h3>10篇畅写</h3>
<div class="big-price">168<small>起</small></div>
<div class="per-unit">省约42% / 低至16.8/篇</div>
<ul>
<li>任选服务自由搭配</li>
<li>专属客服，30分钟响应</li>
<li>送3次免费加急</li>
<li>优先交付+月度对账</li>
</ul>
<button class="cta-btn" style="padding:10px 28px;font-size:.9rem" onclick="openOrder('10篇套餐',168)">立即抢购</button>
</div>
</div>
<h2 class="section-title" style="font-size:1.3rem;margin-bottom:20px">单品价目表</h2>
<div class="pricing-table"><table>
<thead><tr><th>服务项</th><th>说明</th><th style="text-align:center">单价</th><th></th></tr></thead>
<tbody>
<tr><td>小红书笔记</td><td>500-800字 + 标题 + emoji排版 + 话题标签</td><td class="price-cell" style="text-align:center"><span class="old-price">39</span><strong>29</strong> <span class="tag hot">热销</span></td><td class="order-cell"><button class="mini-order-btn" onclick="openOrder('小红书笔记',29)">选我</button></td></tr>
<tr><td>公众号文章</td><td>1500-2000字含小标题和配图建议</td><td class="price-cell" style="text-align:center"><span class="old-price">79</span><strong>59</strong></td><td class="order-cell"><button class="mini-order-btn" onclick="openOrder('公众号文章',59)">选我</button></td></tr>
<tr><td>短视频脚本</td><td>60s口播稿含开头钩子+逻辑框架+CTA</td><td class="price-cell" style="text-align:center"><span class="old-price">59</span><strong>39</strong> <span class="tag pop">火爆</span></td><td class="order-cell"><button class="mini-order-btn" onclick="openOrder('短视频脚本',39)">选我</button></td></tr>
<tr><td>简历优化</td><td>中英文简历排版+措辞润色+一页纸优化</td><td class="price-cell" style="text-align:center"><strong>49</strong></td><td class="order-cell"><button class="mini-order-btn" onclick="openOrder('简历优化',49)">选我</button></td></tr>
<tr><td>PPT制作</td><td>10页以内模板精美含动画/图表</td><td class="price-cell" style="text-align:center"><span class="old-price">149</span><strong>99</strong></td><td class="order-cell"><button class="mini-order-btn" onclick="openOrder('PPT制作',99)">选我</button></td></tr>
<tr><td>AI头像/人像</td><td>Midjourney直出含3版供选</td><td class="price-cell" style="text-align:center"><strong>19</strong> <span class="tag new">入门</span></td><td class="order-cell"><button class="mini-order-btn" onclick="openOrder('AI头像',19)">选我</button></td></tr>
<tr><td>Excel自动化</td><td>VBA/Python脚本去重/合并/报表一键生成</td><td class="price-cell" style="text-align:center"><strong>69</strong></td><td class="order-cell"><button class="mini-order-btn" onclick="openOrder('Excel自动化',69)">选我</button></td></tr>
<tr><td>定制方案</td><td>商业计划书/毕业论文润色/品牌全案</td><td class="price-cell" style="text-align:center"><strong>200+</strong> <span class="tag" style="background:#fff3e0;color:#e65100">议价</span></td><td class="order-cell"><button class="mini-order-btn" onclick="openOrder('定制方案',200)">询价</button></td></tr>
</tbody></table></div>
<p style="text-align:center;margin-top:16px;color:#6e6e73;font-size:.9rem">套餐与单品可混合使用 / 长期合作另议</p>
</div></div>"""

# Find old pricing section
pattern = r'<div class="section" style="background:#f5f5f7".*?</div></div>\s*<div class="section"'
match = re.search(pattern, html, re.DOTALL)
if match:
    old = match.group()
    new = new_pricing + "\n<div class=\"section\""
    html = html.replace(old, new, 1)
    print("Pricing section replaced OK")
else:
    print("WARNING: Could not find pricing section")

# ====== NEW ORDER SECTION ======
# Remove old inquiry section
inquiry_start = html.find('<div class="section"><div class="container">\n<h2 class="section-title">提交需求</h2>')
if inquiry_start == -1:
    inquiry_start = html.find('<h2 class="section-title">提交需求</h2>')
    # Go back to find the opening div
    start_div = html.rfind('<div', 0, inquiry_start)
    if start_div != -1:
        inquiry_start = start_div
inquiry_end = html.find('<div class="footer">', inquiry_start)

new_order_section = """<div class="modal-overlay" id="orderModal">
<div class="modal-box">
<button class="modal-close" onclick="closeOrderModal()">&times;</button>
<h2>快速下单</h2>
<p class="modal-sub">填完需求，复制信息直接微信发我</p>
<form id="quickOrderForm">
<div class="form-row">
<label>服务类型</label>
<select id="qService" onchange="calcTotal()">
<option value="小红书笔记" data-price="29">小红书笔记 - 29</option>
<option value="公众号文章" data-price="59">公众号文章 - 59</option>
<option value="短视频脚本" data-price="39">短视频脚本 - 39</option>
<option value="简历优化" data-price="49">简历优化 - 49</option>
<option value="PPT制作" data-price="99">PPT制作 - 99</option>
<option value="AI头像" data-price="19">AI头像/人像 - 19</option>
<option value="Excel自动化" data-price="69">Excel自动化 - 69</option>
<option value="定制品" data-price="200">定制方案 - 200+</option>
</select>
</div>
<div class="form-row">
<label>数量</label>
<select id="qQuantity" onchange="calcTotal()">
<option value="1">1 篇/份</option>
<option value="3">3 篇/份 (省30-60)</option>
<option value="5">5 篇/份 (省50-100)</option>
<option value="10">10 篇/份 (省100-200)</option>
</select>
</div>
<div class="form-row">
<label>加急</label>
<select id="qUrgent">
<option value="normal">普通（2小时内交付）</option>
<option value="urgent">加急（30分钟内交付）</option>
</select>
</div>
<div class="total-bar">
<span class="total-label">预估总价</span>
<span class="total-amount" id="totalDisplay">29 <small>首单</small></span>
</div>
<div class="form-row">
<label>你的称呼</label>
<input type="text" id="qName" placeholder="怎么称呼你" required>
</div>
<div class="form-row">
<label>联系方式</label>
<input type="text" id="qContact" placeholder="微信号/手机号" required>
</div>
<div class="form-row">
<label>需求说明</label>
<textarea id="qDetail" placeholder="说一下具体要求：什么主题？多少字？什么风格？有什么参考素材？" required></textarea>
</div>
<button type="submit" class="submit-btn">复制订单信息发微信 <span class="sub">-> 发给 dxc629811</span></button>
</form>
</div>
</div>

<button class="float-order" onclick="openOrder()">
&#9993;
<span class="float-label">快速下单</span>
</button>"""

if inquiry_end > inquiry_start:
    html = html[:inquiry_start] + new_order_section + html[inquiry_end:]
    print("Order section replaced OK")
else:
    print("WARNING: Could not find inquiry section")

# ====== NEW JS ======
new_js = """<script>
var priceMap = {
  "小红书笔记":29,"公众号文章":59,"短视频脚本":39,
  "简历优化":49,"PPT制作":99,"AI头像":19,
  "Excel自动化":69,"定制品":200
};
var qtyDiscount = {1:1,3:0.9,5:0.8,10:0.7};

function openOrder(service,price) {
  document.getElementById("orderModal").classList.add("show");
  document.body.style.overflow="hidden";
  if(service) {
    var sel=document.getElementById("qService");
    for(var i=0;i<sel.options.length;i++) {
      if(sel.options[i].value===service){sel.selectedIndex=i;break;}
    }
  }
  calcTotal();
  setTimeout(function(){document.getElementById("qName").focus()},300);
}
function closeOrderModal() {
  document.getElementById("orderModal").classList.remove("show");
  document.body.style.overflow="";
}
function calcTotal() {
  var svc=document.getElementById("qService").value;
  var qty=parseInt(document.getElementById("qQuantity").value);
  var base=priceMap[svc]||29;
  var disc=qtyDiscount[qty]||1;
  var total=Math.round(base*qty*disc);
  var el=document.getElementById("totalDisplay");
  if(qty>1) {
    var saved=base*qty-total;
    el.innerHTML=total+" <small>省"+saved+"</small>";
  } else {
    el.innerHTML=total+" <small>首单</small>";
  }
}
document.getElementById("orderModal").addEventListener("click",function(e){
  if(e.target===this)closeOrderModal();
});
document.addEventListener("keydown",function(e){
  if(e.key==="Escape")closeOrderModal();
});
document.getElementById("quickOrderForm").addEventListener("submit",function(e){
  e.preventDefault();
  var svc=document.getElementById("qService").value;
  var qty=document.getElementById("qQuantity").value;
  var urg=document.getElementById("qUrgent").value;
  var name=document.getElementById("qName").value.trim();
  var ctc=document.getElementById("qContact").value.trim();
  var det=document.getElementById("qDetail").value.trim();
  if(!name||!ctc||!det){alert("请填写完整信息");return;}
  var total=document.getElementById("totalDisplay").innerText;
  var txt="【新订单】\\n客户: "+name+"\\n微信: "+ctc+"\\n服务: "+svc+"\\n数量: "+qty+"\\n加急: "+(urg==="urgent"?"是(30分钟)":"否(2小时)")+"\\n预估: "+total+"\\n需求: "+det+"\\n请加微信: dxc629811";
  var ta=document.createElement("textarea");
  ta.value=txt;ta.style.position="fixed";ta.style.opacity="0";
  document.body.appendChild(ta);ta.select();
  document.execCommand("copy");
  document.body.removeChild(ta);
  var orders=JSON.parse(localStorage.getItem("orders")||"[]");
  orders.unshift({name:name,contact:ctc,service:svc+"x"+qty,detail:det,time:new Date().toLocaleString(),amount:total});
  localStorage.setItem("orders",JSON.stringify(orders));
  var toast=document.getElementById("toast");
  toast.textContent="订单信息已复制！请加微信 dxc629811 发给我";
  toast.classList.add("show");
  setTimeout(function(){toast.classList.remove("show")},4000);
  closeOrderModal();
  this.reset();
  document.getElementById("qQuantity").value="1";
  document.getElementById("qUrgent").value="normal";
  calcTotal();
});
</script>"""

# Replace old JS
js_start = html.find("<script>")
js_end = html.find("</script>") + 9
if js_start != -1 and js_end > js_start:
    html = html[:js_start] + new_js + html[js_end:]
    print("JS replaced OK")
else:
    print("WARNING: Could not find JS")

# Save
open("C:\\Users\\25495\\Desktop\\新建文件夹\\startup-kit\\index.html", "w", encoding="utf-8").write(html)
print("DONE! Final size:", len(html))
