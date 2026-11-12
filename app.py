
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CELL TYCOON",
    page_icon="🧫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {
        background: #f8f8f8;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

GAME = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

* { box-sizing:border-box; }

body {
    margin:0;
    background:#fafafa;
    color:#292533;
    font-family:'Press Start 2P', monospace;
    overflow-x:hidden;
}

button {
    font-family:'Press Start 2P', monospace;
    cursor:pointer;
    border:4px solid #171421;
    box-shadow:4px 4px 0 #171421;
    transition:transform .1s;
}

button:active {
    transform:translate(3px,3px);
    box-shadow:1px 1px 0 #171421;
}

#game {
    width:100%;
    min-height:850px;
    position:relative;
    overflow:hidden;
    background-color:#fff;
    background-image:
        linear-gradient(#d5d5d5 2px, transparent 2px),
        linear-gradient(90deg,#d5d5d5 2px, transparent 2px);
    background-size:60px 60px;
}

#topbar {
    height:60px;
    background:#272332;
    color:white;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 20px;
    font-size:12px;
    position:relative;
    z-index:5;
}

#brand {
    font-size:17px;
    color:#ff5252;
    text-shadow:3px 3px #111;
}

#currency {
    color:#4ee16b;
    font-size:12px;
}

#left {
    position:absolute;
    top:100px;
    left:15px;
    display:flex;
    flex-direction:column;
    gap:25px;
    z-index:4;
}

.sidebutton {
    width:105px;
    height:90px;
    background:#332d40;
    color:white;
    font-size:9px;
    border:4px solid #171421;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    gap:8px;
}

.sideicon {
    font-size:35px;
}

#center {
    position:absolute;
    left:50%;
    top:110px;
    transform:translateX(-50%);
    width:min(650px,65%);
    height:470px;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-wrap:wrap;
    align-content:center;
    gap:35px;
    padding:25px;
}

.ball {
    width:130px;
    height:130px;
    border-radius:38%;
    background:var(--ball);
    border:13px solid var(--dark);
    position:relative;
    box-shadow:
        inset 9px 9px 0 var(--light),
        inset -10px -12px 0 var(--dark),
        8px 13px 15px #0003;
    animation:float 2s ease-in-out infinite alternate;
}

.ball:after {
    content:"";
    position:absolute;
    width:40px;
    height:13px;
    background:#ffffff66;
    top:13px;
    left:18px;
    transform:rotate(-35deg);
    border-radius:10px;
}

@keyframes float {
    from { transform:translateY(-4px); }
    to { transform:translateY(5px); }
}

#stats {
    position:absolute;
    right:18px;
    top:300px;
    width:245px;
    display:flex;
    flex-direction:column;
    gap:12px;
}

.stat {
    background:#2c2736;
    color:#eee5cb;
    border:5px solid #171421;
    box-shadow:5px 5px 0 #171421;
    padding:15px 12px;
    min-height:85px;
    font-size:9px;
    line-height:2.1;
}

.stathead {
    display:flex;
    justify-content:space-between;
    margin-bottom:10px;
}

.price { color:#48e76d; }

#bottom {
    position:absolute;
    bottom:55px;
    left:50%;
    transform:translateX(-50%);
    width:min(850px,90%);
    display:flex;
    gap:20px;
}

.bigbutton {
    flex:1;
    height:120px;
    font-size:22px;
    color:#f6edcf;
    background:#383145;
}

#sell {
    background:#285c3e;
}

#splitinfo {
    position:absolute;
    top:-32px;
    left:20%;
    color:#292333;
    font-size:17px;
    text-shadow:2px 2px white;
}

#skill {
    position:absolute;
    top:90px;
    left:50%;
    transform:translateX(-50%);
    background:#302a3d;
    color:white;
    padding:12px;
    font-size:10px;
    width:140px;
    height:85px;
}

#more {
    position:absolute;
    top:90px;
    left:calc(50% + 90px);
    background:#f6bd3b;
    width:90px;
    height:85px;
    font-size:10px;
}

#message {
    position:absolute;
    top:240px;
    left:50%;
    transform:translateX(-50%);
    background:#302a3d;
    color:#fff;
    padding:14px 20px;
    font-size:10px;
    z-index:10;
    display:none;
    text-align:center;
    max-width:85%;
    line-height:2;
}

#modal {
    display:none;
    position:fixed;
    inset:0;
    background:#0009;
    z-index:20;
    align-items:center;
    justify-content:center;
    padding:15px;
}

#modalbox {
    width:min(600px,95%);
    max-height:80vh;
    overflow:auto;
    background:#302a3d;
    color:#fff0d0;
    border:6px solid #171421;
    box-shadow:8px 8px #0008;
    padding:20px;
}

#modaltitle {
    font-size:15px;
    margin-bottom:20px;
    color:#ffcf56;
}

.item {
    border:3px solid #756b83;
    padding:13px;
    margin:10px 0;
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:10px;
    font-size:9px;
    line-height:2;
}

.item button {
    padding:12px;
    font-size:8px;
    background:#4c9b64;
    color:white;
    white-space:nowrap;
}

.close {
    margin-top:15px;
    background:#d34c4c;
    color:white;
    padding:12px;
    font-size:10px;
}

#notice {
    position:absolute;
    left:50%;
    top:195px;
    transform:translateX(-50%);
    font-size:10px;
    color:#50485b;
}

@media(max-width:700px) {
    #game { min-height:1050px; }
    #topbar {font-size:8px;padding:0 8px;}
    #brand {font-size:11px;}
    #left {
        top:85px;
        left:5px;
        gap:10px;
    }
    .sidebutton {
        width:65px;
        height:65px;
        font-size:7px;
    }
    .sideicon {font-size:23px;}
    #center {
        top:190px;
        width:90%;
        height:350px;
        gap:15px;
    }
    .ball {
        width:85px;
        height:85px;
        border-width:9px;
    }
    #stats {
        top:555px;
        right:8px;
        width:45%;
    }
    .stat {font-size:7px;padding:8px;}
    #skill {top:85px;left:42%;width:100px;font-size:8px;}
    #more {top:85px;left:calc(42% + 110px);width:75px;font-size:8px;}
    #bottom {
        bottom:35px;
        width:95%;
        gap:10px;
    }
    .bigbutton {height:90px;font-size:13px;}
    #notice {top:170px;font-size:8px;}
}
</style>
</head>

<body>
<div id="game">

    <div id="topbar">
        <div id="brand">CELL TYCOON</div>
        <div id="currency">$ <span id="money">0</span></div>
        <div>REBIRTH <span id="rebirths">0</span></div>
    </div>

    <div id="left">
        <button class="sidebutton" onclick="openShop()">
            <span class="sideicon">🛒</span>SHOP
        </button>
        <button class="sidebutton" onclick="rebirth()">
            <span class="sideicon">🔄</span>REBIRTH
        </button>
        <button class="sidebutton" onclick="openCollection()">
            <span class="sideicon">🧬</span>COLLECTION
        </button>
    </div>

    <button id="skill" onclick="openSkills()">
        🟡<br><br>SKILL TREE
    </button>

    <button id="more" onclick="openMore()">
        ⬆<br><br>MORE
    </button>

    <div id="notice">SPLIT YOUR CELLS. GROW YOUR EMPIRE.</div>

    <div id="center"></div>

    <div id="stats">
        <div class="stat">
            <div class="stathead">
                BALL VALUE
                <span class="price">$ <span id="valuecost">10</span></span>
            </div>
            $<span id="value">1</span> &gt; $<span id="nextvalue">2</span> A BALL
        </div>

        <div class="stat">
            <div class="stathead">
                SPLIT SPEED
                <span class="price">$ <span id="speedcost">10</span></span>
            </div>
            <span id="speed">5.0</span> &gt; <span id="nextspeed">4.9</span> SEC
        </div>

        <div class="stat">
            <div class="stathead">
                CAPACITY
                <span class="price">$ <span id="capacitycost">10</span></span>
            </div>
            <span id="capacity">16</span> &gt; <span id="nextcapacity">18</span> BALLS
        </div>
    </div>

    <div id="bottom">
        <div id="splitinfo">X2</div>
        <button class="bigbutton" onclick="splitBalls()">SPLIT</button>
        <button class="bigbutton" id="sell" onclick="sellBalls()">SELL</button>
    </div>

    <div id="message"></div>
</div>

<div id="modal">
    <div id="modalbox">
        <div id="modaltitle">SHOP</div>
        <div id="modalcontent"></div>
        <button class="close" onclick="closeModal()">CLOSE</button>
    </div>
</div>

<script>
const defaultState = {
    money:0,
    balls:2,
    ballValue:1,
    splitSpeed:5,
    capacity:16,
    valueCost:10,
    speedCost:10,
    capacityCost:10,
    rebirths:0,
    skin:"red",
    owned:["red"],
    skills:0,
    totalSold:0,
    totalSplits:0
};

let state = {...defaultState};

try {
    const saved = JSON.parse(localStorage.getItem("cell_tycoon_save"));
    if(saved) state = {...defaultState,...saved};
} catch(e) {}

const skins = {
    red:{name:"Classic Red",color:"#ed1010",dark:"#8c0808",light:"#ff7777",price:0},
    blue:{name:"Ocean Blue",color:"#1687ef",dark:"#07509d",light:"#82d4ff",price:150},
    green:{name:"Toxic Green",color:"#44dc4e",dark:"#168321",light:"#a2ff91",price:300},
    purple:{name:"Royal Purple",color:"#9c54e9",dark:"#53238c",light:"#d5a2ff",price:600},
    gold:{name:"Golden Cell",color:"#ffc52e",dark:"#9d6500",light:"#fff19a",price:1200},
    pink:{name:"Galaxy Pink",color:"#ff66c8",dark:"#a32679",light:"#ffc2e8",price:2500}
};

function save() {
    localStorage.setItem("cell_tycoon_save",JSON.stringify(state));
}

function notify(text) {
    const el = document.getElementById("message");
    el.innerText = text;
    el.style.display = "block";
    clearTimeout(window.noticeTimer);
    window.noticeTimer = setTimeout(()=>el.style.display="none",2200);
}

function render() {
    document.getElementById("money").innerText = Math.floor(state.money).toLocaleString();
    document.getElementById("rebirths").innerText = state.rebirths;
    document.getElementById("value").innerText = state.ballValue;
    document.getElementById("nextvalue").innerText = state.ballValue+1;
    document.getElementById("valuecost").innerText = state.valueCost;
    document.getElementById("speed").innerText = state.splitSpeed.toFixed(1);
    document.getElementById("nextspeed").innerText = Math.max(0.5,state.splitSpeed-0.1).toFixed(1);
    document.getElementById("speedcost").innerText = state.speedCost;
    document.getElementById("capacity").innerText = state.capacity;
    document.getElementById("nextcapacity").innerText = state.capacity+2;
    document.getElementById("capacitycost").innerText = state.capacityCost;

    const center = document.getElementById("center");
    center.innerHTML = "";

    const skin = skins[state.skin] || skins.red;
    const displayCount = Math.min(state.balls,12);

    for(let i=0;i<displayCount;i++) {
        const ball = document.createElement("div");
        ball.className = "ball";
        ball.style.setProperty("--ball",skin.color);
        ball.style.setProperty("--dark",skin.dark);
        ball.style.setProperty("--light",skin.light);
        ball.style.animationDelay = (i*.15)+"s";
        center.appendChild(ball);
    }

    if(state.balls>12) {
        const extra = document.createElement("div");
        extra.style.fontSize="13px";
        extra.style.fontWeight="bold";
        extra.innerText="+"+(state.balls-12)+" MORE";
        center.appendChild(extra);
    }

    save();
}

function splitBalls() {
    if(state.balls>=state.capacity) {
        notify("MAXIMUM CAPACITY! UPGRADE YOUR CAPACITY.");
        return;
    }

    const amount = Math.min(state.balls,state.capacity-state.balls);
    state.balls += amount;
    state.totalSplits++;

    render();
    notify("+"+amount+" NEW CELLS!");
}

function sellBalls() {
    if(state.balls<=0) {
        notify("NO CELLS TO SELL!");
        return;
    }

    const bonus = 1+(state.rebirths*.1)+(state.skills*.05);
    const earned = Math.floor(state.balls*state.ballValue*bonus);

    state.money += earned;
    state.totalSold += state.balls;
    state.balls = 0;

    render();
    notify("SOLD YOUR CELLS! +$"+earned);

    setTimeout(()=>{
        if(state.balls===0) {
            state.balls=2;
            render();
        }
    },700);
}

function buyUpgrade(type) {
    let cost,success=false;

    if(type==="value") {
        cost=state.valueCost;
        if(state.money>=cost) {
            state.money-=cost;
            state.ballValue++;
            state.valueCost=Math.floor(cost*1.65);
            success=true;
        }
    }

    if(type==="speed") {
        cost=state.speedCost;
        if(state.money>=cost && state.splitSpeed>0.5) {
            state.money-=cost;
            state.splitSpeed=Math.max(.5,Math.round((state.splitSpeed-.1)*10)/10);
            state.speedCost=Math.floor(cost*1.7);
            success=true;
        }
    }

    if(type==="capacity") {
        cost=state.capacityCost;
        if(state.money>=cost) {
            state.money-=cost;
            state.capacity+=2;
            state.capacityCost=Math.floor(cost*1.6);
            success=true;
        }
    }

    if(success) {
        render();
        notify("UPGRADE PURCHASED!");
    } else {
        notify("NOT ENOUGH MONEY!");
    }
}

function openModal(title,content) {
    document.getElementById("modaltitle").innerText=title;
    document.getElementById("modalcontent").innerHTML=content;
    document.getElementById("modal").style.display="flex";
}

function closeModal() {
    document.getElementById("modal").style.display="none";
}

function openShop() {
    let html="";

    Object.keys(skins).forEach(id=>{
        const s=skins[id];
        const owned=state.owned.includes(id);
        const equipped=state.skin===id;

        html+=`
        <div class="item">
            <span>
                <span style="color:${s.color};font-size:16px">●</span>
                ${s.name}<br>
                ${s.price===0?"FREE":"$"+s.price}
            </span>
            <button onclick="buySkin('${id}')">
                ${equipped?"EQUIPPED":owned?"EQUIP":"BUY"}
            </button>
        </div>`;
    });

    openModal("CELL SHOP",html);
}

function buySkin(id) {
    const s=skins[id];

    if(state.owned.includes(id)) {
        state.skin=id;
        render();
        openShop();
        notify("SKIN EQUIPPED!");
        return;
    }

    if(state.money<s.price) {
        notify("NOT ENOUGH MONEY!");
        return;
    }

    state.money-=s.price;
    state.owned.push(id);
    state.skin=id;
    render();
    openShop();
    notify("NEW CELL SKIN UNLOCKED!");
}

function openSkills() {
    const html=`
        <div class="item">
            <span>💰 MONEY BOOST<br>+5% selling income<br>Cost: 1 Skill Point</span>
            <button onclick="buySkill('money')">BUY</button>
        </div>
        <div class="item">
            <span>⚡ SPEED BOOST<br>Permanent split bonus<br>Cost: 2 Skill Points</span>
            <button onclick="buySkill('speed')">BUY</button>
        </div>
        <div class="item">
            <span>🧬 CELL BOOST<br>Extra starting cells<br>Cost: 3 Skill Points</span>
            <button onclick="buySkill('cells')">BUY</button>
        </div>
        <p>Available Skill Points: ${state.skills}</p>
    `;
    openModal("SKILL TREE",html);
}

function buySkill(type) {
    const costs={money:1,speed:2,cells:3};
    const cost=costs[type];

    if(state.skills<cost) {
        notify("NOT ENOUGH SKILL POINTS!");
        return;
    }

    state.skills-=cost;

    if(type==="money") {
        state.ballValue+=1;
    }

    if(type==="speed") {
        state.splitSpeed=Math.max(.5,state.splitSpeed-.2);
    }

    if(type==="cells") {
        state.balls+=2;
        state.capacity+=2;
    }

    render();
    openSkills();
    notify("SKILL UNLOCKED!");
}

function rebirth() {
    const requirement=10000*(state.rebirths+1);

    if(state.money<requirement) {
        notify("YOU NEED $"+requirement.toLocaleString()+" TO REBIRTH!");
        return;
    }

    if(!confirm("REBIRTH NOW? Your money and upgrades will reset, but you will gain 1 Skill Point and a permanent bonus.")) return;

    state.money=0;
    state.balls=2;
    state.ballValue=1;
    state.splitSpeed=5;
    state.capacity=16;
    state.valueCost=10;
    state.speedCost=10;
    state.capacityCost=10;
    state.rebirths++;
    state.skills++;
    state.totalSplits=0;

    render();
    notify("REBIRTH COMPLETE! +1 SKILL POINT!");
}

function openCollection() {
    let html=`
        <div class="item">
            <span>CELLS SOLD</span>
            <span>${state.totalSold}</span>
        </div>
        <div class="item">
            <span>TOTAL SPLITS</span>
            <span>${state.totalSplits}</span>
        </div>
        <div class="item">
            <span>SKINS OWNED</span>
            <span>${state.owned.length}/${Object.keys(skins).length}</span>
        </div>
        <div class="item">
            <span>REBIRTHS</span>
            <span>${state.rebirths}</span>
        </div>
    `;
    openModal("YOUR COLLECTION",html);
}

function openMore() {
    const html=`
        <div class="item">
            <span>GAME GUIDE<br>Split your cells, sell them, and upgrade your lab.</span>
        </div>
        <div class="item">
            <span>YOUR BONUS<br>${state.rebirths*10}% rebirth bonus</span>
        </div>
        <div class="item">
            <span>PROGRESS<br>$${Math.floor(state.money).toLocaleString()} cash</span>
        </div>
        <div class="item">
            <span>DATA<br>Progress saves automatically in this browser.</span>
        </div>
        <button onclick="resetGame()" style="padding:12px;background:#b53b3b;color:white;font-size:9px;">RESET SAVE</button>
    `;
    openModal("MORE",html);
}

function resetGame() {
    if(!confirm("Are you sure? This will erase your saved game.")) return;
    state={...defaultState,owned:["red"]};
    render();
    closeModal();
    notify("NEW GAME STARTED!");
}

render();
</script>
</body>
</html>
"""

components.html(GAME, height=900, scrolling=True)
