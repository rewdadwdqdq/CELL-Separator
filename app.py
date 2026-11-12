
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cell Tycoon",
    page_icon="🧫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

GAME = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
*{box-sizing:border-box}
body{
    margin:0;
    background:#090d18;
    color:#f4f6ff;
    font-family:Arial,Helvetica,sans-serif;
}
button{font-family:inherit}
#game{
    max-width:1250px;
    margin:auto;
    padding:18px;
}
.topbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:12px;
    flex-wrap:wrap;
    margin-bottom:16px;
}
.logo{
    font-size:27px;
    font-weight:900;
    letter-spacing:1px;
}
.logo span{color:#6ee7ff}
.stats{
    display:flex;
    gap:9px;
    flex-wrap:wrap;
}
.stat{
    background:#151d31;
    border:1px solid #293653;
    border-radius:12px;
    padding:10px 14px;
    min-width:105px;
}
.stat small{
    display:block;
    color:#9eabc8;
    font-size:11px;
    margin-bottom:4px;
}
.stat strong{font-size:18px}
.main{
    display:grid;
    grid-template-columns:230px minmax(300px,1fr) 230px;
    gap:14px;
}
.panel{
    background:#11192b;
    border:1px solid #263451;
    border-radius:16px;
    padding:15px;
}
.panel h3{
    margin:0 0 13px;
    font-size:16px;
}
.upgrade{
    width:100%;
    border:1px solid #344666;
    background:#1b2943;
    color:white;
    border-radius:12px;
    padding:12px;
    text-align:left;
    margin-bottom:9px;
    cursor:pointer;
    transition:transform .12s,background .12s,box-shadow .12s;
}
.upgrade:hover{background:#263957}
.upgrade:active,.action:active,.navbtn:active,.skill:active{
    transform:translateY(4px) scale(.98);
    box-shadow:inset 0 4px 8px #0008;
}
.upgrade:disabled,.action:disabled,.skill:disabled{
    opacity:.42;
    cursor:not-allowed;
}
.upgrade b{display:block;font-size:13px;margin-bottom:5px}
.upgrade small{color:#a9b8d7;line-height:1.4}
.center{
    min-height:540px;
    position:relative;
    overflow:hidden;
    background:
      radial-gradient(ellipse at center,#1c3150 0%,#101a2d 55%,#0d1423 100%);
    border:1px solid #304363;
    border-radius:18px;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    padding:20px;
}
.center h2{margin:0 0 6px;font-size:23px}
.subtitle{color:#9eabc8;font-size:13px;margin-bottom:25px}
.cell-area{
    width:100%;
    height:260px;
    position:relative;
    display:flex;
    justify-content:center;
    align-items:center;
}
.cell{
    width:48px;
    height:48px;
    position:absolute;
    border-radius:50%;
    background:radial-gradient(circle at 32% 28%,#fff 0%,var(--cell) 22%,#173c76 100%);
    border:2px solid #ffffff9c;
    box-shadow:0 0 18px var(--glow),inset -5px -6px 10px #0005;
    display:flex;
    align-items:center;
    justify-content:center;
    z-index:2;
}
.nucleus{
    width:15px;height:15px;border-radius:50%;
    background:#b9a2ff;
    border:2px solid #ffffff99;
    box-shadow:0 0 9px #b9a2ff;
}
.cell-count{
    font-size:36px;
    font-weight:900;
    margin-top:8px;
}
.cell-label{color:#aab8d4;font-size:12px;margin-top:2px}
.actions{
    display:flex;
    justify-content:center;
    gap:12px;
    flex-wrap:wrap;
    margin-top:22px;
}
.action{
    border:0;
    border-radius:12px;
    padding:14px 24px;
    color:#07111e;
    font-weight:900;
    cursor:pointer;
    min-width:135px;
    transition:transform .12s,filter .12s;
}
.action:hover{filter:brightness(1.12)}
.split{background:linear-gradient(135deg,#70f0ff,#4c9eff)}
.sell{background:linear-gradient(135deg,#ffd66e,#ff9d4c)}
.cooldowns{
    display:flex;
    gap:10px;
    flex-wrap:wrap;
    justify-content:center;
    margin-top:15px;
}
.cooldown{
    font-size:12px;
    color:#c6d3ed;
    background:#111a2b;
    border:1px solid #344666;
    border-radius:9px;
    padding:8px 11px;
}
.nav{
    display:flex;
    gap:8px;
    flex-wrap:wrap;
    margin:14px 0;
}
.navbtn{
    background:#17233a;
    border:1px solid #304363;
    color:#dce7ff;
    padding:10px 15px;
    border-radius:10px;
    cursor:pointer;
    transition:transform .12s,background .12s;
}
.navbtn.active{background:#28517a;border-color:#6ee7ff}
.bottom{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:14px;
}
.progressbar{
    height:9px;
    background:#26344e;
    border-radius:20px;
    overflow:hidden;
    margin-top:9px;
}
.progressbar div{
    height:100%;
    background:linear-gradient(90deg,#5ce7ff,#8d8aff);
    width:0%;
}
.modal{
    display:none;
    position:fixed;
    inset:0;
    background:#000b;
    z-index:50;
    align-items:center;
    justify-content:center;
    padding:15px;
}
.modal.show{display:flex}
.modalbox{
    width:min(720px,100%);
    max-height:85vh;
    overflow:auto;
    background:#111a2d;
    border:1px solid #405477;
    border-radius:18px;
    padding:20px;
    box-shadow:0 20px 80px #0009;
}
.modalhead{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:15px;
}
.modalhead h2{margin:0}
.close{
    background:#263653;
    color:white;
    border:0;
    border-radius:9px;
    padding:8px 12px;
    cursor:pointer;
}
.items{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(170px,1fr));
    gap:10px;
}
.item{
    background:#1a2740;
    border:1px solid #354968;
    border-radius:12px;
    padding:13px;
}
.item h4{margin:0 0 7px}
.item p{font-size:12px;color:#aab8d4;min-height:30px}
.item button,.skill button{
    width:100%;
    padding:9px;
    border:0;
    border-radius:9px;
    background:#4dbce8;
    color:#07111e;
    font-weight:bold;
    cursor:pointer;
    transition:transform .12s;
}
.item button:disabled{opacity:.4;cursor:not-allowed}
.skillgrid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(160px,1fr));
    gap:10px;
}
.skill{
    background:#1a2740;
    border:1px solid #354968;
    border-radius:12px;
    padding:13px;
}
.skill h4{margin:0 0 7px}
.skill p{font-size:12px;color:#aab8d4;min-height:32px}
.notice{
    color:#9eabc8;
    font-size:12px;
    line-height:1.5;
    margin-top:10px;
}
.toast{
    position:fixed;
    bottom:18px;
    left:50%;
    transform:translateX(-50%) translateY(20px);
    opacity:0;
    background:#e9f8ff;
    color:#101827;
    font-weight:bold;
    border-radius:10px;
    padding:11px 17px;
    z-index:100;
    transition:.2s;
    pointer-events:none;
}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.split-overlay{
    position:absolute;
    inset:0;
    pointer-events:none;
}
.split-daughter{
    position:absolute;
    left:50%;top:50%;
    width:48px;height:48px;
    margin:-24px;
    border-radius:50%;
    background:radial-gradient(circle at 32% 28%,#fff 0%,var(--cell) 22%,#173c76 100%);
    border:2px solid #ffffffaa;
    box-shadow:0 0 18px var(--glow);
    animation-duration:.7s;
    animation-fill-mode:forwards;
}
.split-daughter:after{
    content:"";
    position:absolute;
    width:15px;height:15px;
    border-radius:50%;
    background:#b9a2ff;
    border:2px solid #ffffff99;
    left:14px;top:14px;
}
.split-daughter.left{animation-name:moveLeft}
.split-daughter.right{animation-name:moveRight}
@keyframes moveLeft{
    0%{transform:translate(0,0) scale(.7);opacity:1}
    45%{transform:translate(-35px,-8px) scale(1.2)}
    100%{transform:translate(-75px,0) scale(1);opacity:0}
}
@keyframes moveRight{
    0%{transform:translate(0,0) scale(.7);opacity:1}
    45%{transform:translate(35px,8px) scale(1.2)}
    100%{transform:translate(75px,0) scale(1);opacity:0}
}
.selling-ball{
    position:absolute;
    width:48px;height:48px;
    border-radius:50%;
    background:var(--cell);
    border:2px solid #ffffffaa;
    box-shadow:0 0 18px var(--glow);
    animation:sellAway .5s ease-in forwards;
}
@keyframes sellAway{
    0%{transform:scale(1);opacity:1}
    100%{transform:translateY(-100px) scale(.1);opacity:0}
}
@media(max-width:850px){
    .main{grid-template-columns:1fr}
    .center{min-height:460px;grid-row:1}
    .bottom{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div id="game">
    <div class="topbar">
        <div class="logo">🧫 CELL <span>TYCOON</span></div>
        <div class="stats">
            <div class="stat"><small>💵 MONEY</small><strong id="money">$0</strong></div>
            <div class="stat"><small>🧫 CELLS</small><strong id="cells">1 / 16</strong></div>
            <div class="stat"><small>⭐ REBIRTHS</small><strong id="rebirths">0</strong></div>
            <div class="stat"><small>✨ SKILL POINTS</small><strong id="points">0</strong></div>
        </div>
    </div>

    <div class="main">
        <div class="panel">
            <h3>⬆️ CELL UPGRADES</h3>
            <button class="upgrade" id="valueUpgrade" onclick="buyUpgrade('value')">
                <b>💰 Cell Value</b>
                <small id="valueInfo">Earn more money per cell</small>
            </button>
            <button class="upgrade" id="speedUpgrade" onclick="buyUpgrade('speed')">
                <b>⚡ Split Speed</b>
                <small id="speedInfo">Reduce split cooldown</small>
            </button>
            <button class="upgrade" id="capacityUpgrade" onclick="buyUpgrade('capacity')">
                <b>🧬 Cell Capacity</b>
                <small id="capacityInfo">Hold more cells</small>
            </button>
            <div class="notice">Upgrade your cells to grow faster and earn more money.</div>
        </div>

        <div class="center" id="center">
            <h2>Your Cell Lab</h2>
            <div class="subtitle">Grow your cell population through mitosis.</div>
            <div class="cell-area" id="cellArea">
                <div id="cellContainer"></div>
            </div>
            <div class="cell-count" id="bigCount">1</div>
            <div class="cell-label">TOTAL CELLS</div>
            <div class="actions">
                <button class="action split" id="splitBtn" onclick="splitCells()">🧬 SPLIT CELLS</button>
                <button class="action sell" id="sellBtn" onclick="sellCells()">💰 SELL CELLS</button>
            </div>
            <div class="cooldowns">
                <div class="cooldown" id="splitCooldown">SPLIT READY!</div>
                <div class="cooldown" id="sellCooldown">SELL READY!</div>
            </div>
        </div>

        <div class="panel">
            <h3>🧪 LAB INFORMATION</h3>
            <div class="stat" style="margin-bottom:9px">
                <small>CELL VALUE</small>
                <strong id="cellValue">$1</strong>
            </div>
            <div class="stat" style="margin-bottom:9px">
                <small>SPLIT COOLDOWN</small>
                <strong id="splitSpeedText">5.0s</strong>
            </div>
            <div class="stat" style="margin-bottom:9px">
                <small>MAX CAPACITY</small>
                <strong id="capacityText">16</strong>
            </div>
            <div class="stat">
                <small>CELLS SOLD</small>
                <strong id="soldText">0</strong>
            </div>
            <div class="notice">Selling keeps one cell in your lab, so you can continue growing.</div>
        </div>
    </div>

    <div class="nav">
        <button class="navbtn" onclick="openModal('shopModal')">🛒 Shop</button>
        <button class="navbtn" onclick="openModal('skillModal')">🌳 Skill Tree</button>
        <button class="navbtn" onclick="openModal('collectionModal')">📚 Collection</button>
        <button class="navbtn" onclick="openModal('rebirthModal')">⭐ Rebirth</button>
        <button class="navbtn" onclick="openModal('helpModal')">❔ Help</button>
    </div>

    <div class="bottom">
        <div class="panel">
            <h3>📈 POPULATION PROGRESS</h3>
            <div style="display:flex;justify-content:space-between;font-size:12px">
                <span>Cells</span><span id="progressText">1 / 16</span>
            </div>
            <div class="progressbar"><div id="progressFill"></div></div>
            <div class="notice" id="progressMessage">Split your cell to begin growing.</div>
        </div>
        <div class="panel">
            <h3>🏆 LAB RECORDS</h3>
            <div style="display:flex;justify-content:space-between;margin:8px 0">
                <span style="color:#aab8d4">Total splits</span><b id="splitRecord">0</b>
            </div>
            <div style="display:flex;justify-content:space-between;margin:8px 0">
                <span style="color:#aab8d4">Total cells sold</span><b id="soldRecord">0</b>
            </div>
            <div style="display:flex;justify-content:space-between;margin:8px 0">
                <span style="color:#aab8d4">Highest population</span><b id="bestRecord">1</b>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="shopModal">
 <div class="modalbox">
  <div class="modalhead"><h2>🛒 Cell Skin Shop</h2><button class="close" onclick="closeModal('shopModal')">✕</button></div>
  <div class="items" id="shopItems"></div>
  <div class="notice">Skins are cosmetic and do not change your cell stats.</div>
 </div>
</div>

<div class="modal" id="skillModal">
 <div class="modalbox">
  <div class="modalhead"><h2>🌳 Skill Tree</h2><button class="close" onclick="closeModal('skillModal')">✕</button></div>
  <p class="notice">Spend Skill Points earned from Rebirth to permanently improve your lab.</p>
  <div class="skillgrid" id="skillItems"></div>
 </div>
</div>

<div class="modal" id="collectionModal">
 <div class="modalbox">
  <div class="modalhead"><h2>📚 Cell Collection</h2><button class="close" onclick="closeModal('collectionModal')">✕</button></div>
  <div class="items" id="collectionItems"></div>
 </div>
</div>

<div class="modal" id="rebirthModal">
 <div class="modalbox">
  <div class="modalhead"><h2>⭐ Rebirth Lab</h2><button class="close" onclick="closeModal('rebirthModal')">✕</button></div>
  <p>Rebirth resets your regular upgrades and money, but gives you Skill Points for permanent upgrades.</p>
  <div class="item">
    <h4>Rebirth requirement</h4>
    <p id="rebirthRequirement">Reach 100 cells and $1,000.</p>
    <button id="rebirthButton" onclick="doRebirth()">REBIRTH</button>
  </div>
  <div class="notice">Your collection and purchased skins will be kept.</div>
 </div>
</div>

<div class="modal" id="helpModal">
 <div class="modalbox">
  <div class="modalhead"><h2>❔ How to Play</h2><button class="close" onclick="closeModal('helpModal')">✕</button></div>
  <p><b>1. Split:</b> Press Split Cells to double your cell population.</p>
  <p><b>2. Upgrade:</b> Improve cell value, split speed, and capacity.</p>
  <p><b>3. Sell:</b> Sell your population for money. One cell always remains.</p>
  <p><b>4. Shop:</b> Buy different cell skins with your money.</p>
  <p><b>5. Skill Tree:</b> Use Skill Points from Rebirth for permanent boosts.</p>
  <p><b>6. Rebirth:</b> Reset your normal progress to earn Skill Points.</p>
  <div class="notice">Your progress is saved in this browser. Clearing browser storage may erase it.</div>
 </div>
</div>

<div class="toast" id="toast"></div>

<script>
const SAVE_KEY = "cell_tycoon_save_v4";

const DEFAULT_STATE = {
    money:0,
    balls:1,
    ballValue:1,
    splitSpeed:5,
    capacity:16,
    valueLevel:0,
    speedLevel:0,
    capacityLevel:0,
    valueCost:10,
    speedCost:20,
    capacityCost:25,
    rebirths:0,
    skillPoints:0,
    skills:{money:0,speed:0,cells:0},
    skin:"red",
    ownedSkins:["red"],
    totalSplits:0,
    totalSold:0,
    bestPopulation:1,
    version:4
};

let state = loadGame();

const SKINS = {
    red:{name:"Ruby",color:"#ff596d",glow:"#ff596d",price:0},
    blue:{name:"Ocean",color:"#42a5ff",glow:"#42a5ff",price:250},
    green:{name:"Emerald",color:"#43e59b",glow:"#43e59b",price:500},
    purple:{name:"Galaxy",color:"#b47aff",glow:"#b47aff",price:1000},
    gold:{name:"Golden",color:"#ffd45e",glow:"#ffd45e",price:2500},
    pink:{name:"Candy",color:"#ff80cb",glow:"#ff80cb",price:5000}
};

let nextSplit = 0;
let nextSell = 0;
let splitting = false;
let selling = false;
const SPLIT_ANIMATION_TIME = 700;
const SELL_ANIMATION_TIME = 500;
const SELL_COOLDOWN = 3000;

function loadGame(){
    try{
        const saved = JSON.parse(localStorage.getItem(SAVE_KEY));
        if(saved && saved.version === 4){
            return {...structuredClone(DEFAULT_STATE),...saved,
                skills:{...DEFAULT_STATE.skills,...(saved.skills||{})}};
        }
    }catch(e){}
    return structuredClone(DEFAULT_STATE);
}

function saveGame(){
    try{localStorage.setItem(SAVE_KEY,JSON.stringify(state));}
    catch(e){showToast("Could not save in this browser.");}
}

function formatMoney(value){
    if(value >= 1e12) return "$"+(value/1e12).toFixed(2)+"T";
    if(value >= 1e9) return "$"+(value/1e9).toFixed(2)+"B";
    if(value >= 1e6) return "$"+(value/1e6).toFixed(2)+"M";
    if(value >= 1e3) return "$"+(value/1e3).toFixed(2)+"K";
    return "$"+Math.floor(value).toLocaleString();
}

function showToast(message){
    const toast=document.getElementById("toast");
    toast.textContent=message;
    toast.classList.add("show");
    clearTimeout(showToast.timer);
    showToast.timer=setTimeout(()=>toast.classList.remove("show"),1800);
}

function getMoneyMultiplier(){
    return 1 + state.skills.money * 0.15 + state.rebirths * 0.05;
}

function getSpeedMultiplier(){
    return Math.max(0.5,1 - state.skills.speed * 0.06);
}

function getCapacityBonus(){
    return state.skills.cells * 8;
}

function renderCells(){
    const container=document.getElementById("cellContainer");
    container.innerHTML="";
    const count=state.balls;
    const shown=Math.min(count,36);
    const skin=SKINS[state.skin] || SKINS.red;
    container.style.position="absolute";
    container.style.inset="0";
    for(let i=0;i<shown;i++){
        const cell=document.createElement("div");
        cell.className="cell";
        cell.style.setProperty("--cell",skin.color);
        cell.style.setProperty("--glow",skin.glow);
        const angle=(i/shown)*Math.PI*2;
        const radius=shown===1?0:(Math.min(95,18+shown*2.2));
        const x=Math.cos(angle)*radius;
        const y=Math.sin(angle)*radius;
        cell.style.transform=`translate(${x}px,${y}px)`;
        cell.innerHTML='<div class="nucleus"></div>';
        container.appendChild(cell);
    }
    if(count>36){
        const extra=document.createElement("div");
        extra.style.position="absolute";
        extra.style.bottom="4px";
        extra.style.right="8px";
        extra.style.color="white";
        extra.style.fontWeight="bold";
        extra.textContent="+"+(count-36)+" more";
        container.appendChild(extra);
    }
}

function render(){
    document.getElementById("money").textContent=formatMoney(state.money);
    document.getElementById("cells").textContent=state.balls+" / "+state.capacity;
    document.getElementById("rebirths").textContent=state.rebirths;
    document.getElementById("points").textContent=state.skillPoints;
    document.getElementById("bigCount").textContent=state.balls;
    document.getElementById("cellValue").textContent=formatMoney(state.ballValue);
    document.getElementById("splitSpeedText").textContent=state.splitSpeed.toFixed(1)+"s";
    document.getElementById("capacityText").textContent=state.capacity;
    document.getElementById("soldText").textContent=state.totalSold;
    document.getElementById("splitRecord").textContent=state.totalSplits;
    document.getElementById("soldRecord").textContent=state.totalSold;
    document.getElementById("bestRecord").textContent=state.bestPopulation;

    document.getElementById("valueInfo").textContent=
        "Earn "+formatMoney(state.ballValue)+" per cell sold • Cost: "+formatMoney(state.valueCost);
    document.getElementById("speedInfo").textContent=
        "Current cooldown: "+state.splitSpeed.toFixed(1)+"s • Cost: "+formatMoney(state.speedCost);
    document.getElementById("capacityInfo").textContent=
        "Maximum: "+state.capacity+" cells • Cost: "+formatMoney(state.capacityCost);

    document.getElementById("valueUpgrade").disabled=state.money<state.valueCost;
    document.getElementById("speedUpgrade").disabled=state.money<state.speedCost || state.splitSpeed<=0.7;
    document.getElementById("capacityUpgrade").disabled=state.money<state.capacityCost;

    const progress=Math.min(100,(state.balls/state.capacity)*100);
    document.getElementById("progressFill").style.width=progress+"%";
    document.getElementById("progressText").textContent=state.balls+" / "+state.capacity;
    document.getElementById("progressMessage").textContent=
        state.balls>=state.capacity ? "Your lab is full! Upgrade capacity or sell your cells." :
        "You can grow "+(state.capacity-state.balls)+" more cells before reaching capacity.";

    document.getElementById("rebirthRequirement").textContent=
        "Reach 100 cells and $1,000. Current: "+state.balls+" cells and "+formatMoney(state.money)+".";
    document.getElementById("rebirthButton").disabled=!(state.balls>=100 && state.money>=1000);

    renderCells();
    updateCooldown();
    saveGame();
}

function buyUpgrade(type){
    if(type==="value"){
        if(state.money<state.valueCost)return;
        state.money-=state.valueCost;
        state.valueLevel++;
        state.ballValue+=1;
        state.valueCost=Math.ceil(state.valueCost*1.65);
        showToast("Cell value upgraded!");
    }
    if(type==="speed"){
        if(state.money<state.speedCost || state.splitSpeed<=0.7)return;
        state.money-=state.speedCost;
        state.speedLevel++;
        state.splitSpeed=Math.max(0.7,state.splitSpeed*0.88);
        state.speedCost=Math.ceil(state.speedCost*1.8);
        showToast("Split speed upgraded!");
    }
    if(type==="capacity"){
        if(state.money<state.capacityCost)return;
        state.money-=state.capacityCost;
        state.capacityLevel++;
        state.capacity+=8;
        state.capacityCost=Math.ceil(state.capacityCost*1.7);
        showToast("Cell capacity upgraded!");
    }
    render();
}

function splitCells(){
    const now=Date.now();
    if(splitting || selling)return;
    if(now<nextSplit)return;
    if(state.balls>=state.capacity){
        showToast("Your lab is full! Upgrade capacity.");
        return;
    }

    const oldCount=state.balls;
    const newCount=Math.min(state.capacity,oldCount*2);
    const skin=SKINS[state.skin] || SKINS.red;
    const area=document.getElementById("cellArea");
    const overlay=document.createElement("div");
    overlay.className="split-overlay";

    const pairCount=Math.min(10,Math.max(1,oldCount));
    for(let i=0;i<pairCount;i++){
        const left=document.createElement("div");
        const right=document.createElement("div");
        left.className="split-daughter left";
        right.className="split-daughter right";
        [left,right].forEach(cell=>{
            cell.style.setProperty("--cell",skin.color);
            cell.style.setProperty("--glow",skin.glow);
        });
        const angle=(i/pairCount)*Math.PI*2;
        const radius=oldCount===1?0:Math.min(70,oldCount*2);
        const x=Math.cos(angle)*radius;
        const y=Math.sin(angle)*radius;
        left.style.left=`calc(50% + ${x}px)`;
        left.style.top=`calc(50% + ${y}px)`;
        right.style.left=`calc(50% + ${x}px)`;
        right.style.top=`calc(50% + ${y}px)`;
        overlay.appendChild(left);
        overlay.appendChild(right);
    }
    area.appendChild(overlay);

    splitting=true;
    nextSplit=now+state.splitSpeed*1000;
    state.balls=newCount;
    state.totalSplits++;
    state.bestPopulation=Math.max(state.bestPopulation,state.balls);
    render();
    setTimeout(()=>{
        overlay.remove();
        splitting=false;
        render();
    },SPLIT_ANIMATION_TIME);
}

function sellCells(){
    const now=Date.now();
    if(selling || splitting)return;
    if(now<nextSell)return;
    if(state.balls<=1){
        showToast("You need more than one cell to sell.");
        return;
    }

    const amount=state.balls-1;
    const earned=Math.floor(amount*state.ballValue*getMoneyMultiplier());
    const area=document.getElementById("cellArea");
    const skin=SKINS[state.skin] || SKINS.red;

    for(let i=0;i<Math.min(amount,12);i++){
        const ball=document.createElement("div");
        ball.className="selling-ball";
        ball.style.setProperty("--cell",skin.color);
        ball.style.setProperty("--glow",skin.glow);
        ball.style.left=(25+Math.random()*50)+"%";
        ball.style.top=(25+Math.random()*50)+"%";
        area.appendChild(ball);
        setTimeout(()=>ball.remove(),SELL_ANIMATION_TIME+50);
    }

    selling=true;
    nextSell=now+SELL_COOLDOWN;
    state.money+=earned;
    state.totalSold+=amount;
    state.balls=1;
    render();
    showToast("Sold "+amount+" cells for "+formatMoney(earned)+"!");

    setTimeout(()=>{
        selling=false;
        render();
    },SELL_ANIMATION_TIME);
}

function updateCooldown(){
    const now=Date.now();
    const splitRemaining=Math.max(0,nextSplit-now);
    const sellRemaining=Math.max(0,nextSell-now);

    document.getElementById("splitCooldown").textContent=
        splitRemaining>0 ? "SPLIT READY IN "+(splitRemaining/1000).toFixed(1)+"s" : "SPLIT READY!";
    document.getElementById("sellCooldown").textContent=
        sellRemaining>0 ? "SELL READY IN "+(sellRemaining/1000).toFixed(1)+"s" : "SELL READY!";

    document.getElementById("splitBtn").disabled=
        splitting || selling || splitRemaining>0 || state.balls>=state.capacity;
    document.getElementById("sellBtn").disabled=
        splitting || selling || sellRemaining>0 || state.balls<=1;
}

function openModal(id){
    document.getElementById(id).classList.add("show");
    if(id==="shopModal")renderShop();
    if(id==="skillModal")renderSkills();
    if(id==="collectionModal")renderCollection();
}
function closeModal(id){document.getElementById(id).classList.remove("show");}

function renderShop(){
    const root=document.getElementById("shopItems");
    root.innerHTML="";
    Object.entries(SKINS).forEach(([id,skin])=>{
        const owned=state.ownedSkins.includes(id);
        const selected=state.skin===id;
        const card=document.createElement("div");
        card.className="item";
        card.innerHTML=`
            <div style="height:55px;display:flex;align-items:center;justify-content:center">
              <div style="width:38px;height:38px;border-radius:50%;background:${skin.color};box-shadow:0 0 20px ${skin.glow};border:2px solid white"></div>
            </div>
            <h4>${skin.name} Cell</h4>
            <p>${selected?"Currently equipped":owned?"Already owned":"A new look for your cell"}</p>
            <button ${selected?"disabled":""} onclick="buySkin('${id}')">
              ${selected?"EQUIPPED":owned?"EQUIP":formatMoney(skin.price)}
            </button>`;
        root.appendChild(card);
    });
}

function buySkin(id){
    const skin=SKINS[id];
    if(!skin)return;
    if(state.ownedSkins.includes(id)){
        state.skin=id;
        showToast(skin.name+" skin equipped!");
    }else{
        if(state.money<skin.price){
            showToast("Not enough money!");
            return;
        }
        state.money-=skin.price;
        state.ownedSkins.push(id);
        state.skin=id;
        showToast(skin.name+" skin purchased!");
    }
    render();
    renderShop();
}

function renderSkills(){
    const root=document.getElementById("skillItems");
    root.innerHTML="";
    const skillData=[
        {id:"money",name:"💵 Money Boost",desc:"+15% money earned per level.",max:10},
        {id:"speed",name:"⚡ Quick Division",desc:"Reduce split cooldown by 6% per level.",max:5},
        {id:"cells",name:"🧬 Bigger Lab",desc:"+8 cell capacity per level.",max:10}
    ];
    skillData.forEach(skill=>{
        const level=state.skills[skill.id]||0;
        const cost=level+1;
        const card=document.createElement("div");
        card.className="skill";
        card.innerHTML=`
            <h4>${skill.name}</h4>
            <p>${skill.desc}</p>
            <p><b>Level: ${level}/${skill.max}</b></p>
            <button ${state.skillPoints<cost||level>=skill.max?"disabled":""}
                onclick="buySkill('${skill.id}')">
                Upgrade • ${cost} Point${cost===1?"":"s"}
            </button>`;
        root.appendChild(card);
    });
}

function buySkill(id){
    const max={money:10,speed:5,cells:10};
    const level=state.skills[id]||0;
    const cost=level+1;
    if(level>=max[id]||state.skillPoints<cost)return;
    state.skillPoints-=cost;
    state.skills[id]=level+1;

    if(id==="speed"){
        state.splitSpeed=Math.max(0.7,state.splitSpeed*0.94);
    }
    if(id==="cells"){
        state.capacity+=8;
    }
    showToast("Skill upgraded!");
    render();
    renderSkills();
}

function renderCollection(){
    const root=document.getElementById("collectionItems");
    root.innerHTML="";
    const items=[
        ["First Cell","Start your laboratory.",true],
        ["Growing Lab","Reach 10 cells.",state.bestPopulation>=10],
        ["Cell Colony","Reach 50 cells.",state.bestPopulation>=50],
        ["Cell Empire","Reach 100 cells.",state.bestPopulation>=100],
        ["First Sale","Sell your first cell.",state.totalSold>=1],
        ["Cell Merchant","Sell 100 cells in total.",state.totalSold>=100],
        ["First Rebirth","Rebirth for the first time.",state.rebirths>=1],
        ["Experienced Scientist","Reach 5 Rebirths.",state.rebirths>=5]
    ];
    items.forEach(([name,desc,unlocked])=>{
        const card=document.createElement("div");
        card.className="item";
        card.innerHTML=`
          <h4>${unlocked?"🏆":"🔒"} ${name}</h4>
          <p>${desc}</p>
          <b style="font-size:12px;color:${unlocked?"#70efb4":"#aab8d4"}">
            ${unlocked?"UNLOCKED":"LOCKED"}
          </b>`;
        root.appendChild(card);
    });
}

function doRebirth(){
    if(state.balls<100||state.money<1000)return;
    const pointsEarned=1+Math.floor(state.rebirths/2);
    state.rebirths++;
    state.skillPoints+=pointsEarned;

    state.money=0;
    state.balls=1;
    state.ballValue=1;
    state.splitSpeed=5*Math.pow(0.94,state.skills.speed);
    state.capacity=16+(state.skills.cells*8);
    state.valueLevel=0;
    state.speedLevel=0;
    state.capacityLevel=0;
    state.valueCost=10;
    state.speedCost=20;
    state.capacityCost=25;
    nextSplit=0;
    nextSell=0;

    showToast("Rebirth complete! +" + pointsEarned + " Skill Points!");
    render();
    renderSkills();
    closeModal("rebirthModal");
}

document.querySelectorAll(".modal").forEach(modal=>{
    modal.addEventListener("click",event=>{
        if(event.target===modal)modal.classList.remove("show");
    });
});

setInterval(updateCooldown,100);
render();
</script>
</body>
</html>
"""

components.html(GAME, height=1120, scrolling=True)
