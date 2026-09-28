// Node 18+ | gemini-omni-1.1-flash-ext-reverse-api-ko
const BASE = "https://api.apimart.ai/v1";
const H = { "Authorization": `Bearer ${process.env.APIMART_KEY}`,
             "Content-Type": "application/json" };

const r = await fetch(`${BASE}/videos/generations`, {
  method: "POST", headers: H,
  body: JSON.stringify({ model: "Omni-Flash-Ext", prompt: "cozy reading nook, warm lamp, cinematic"
     , duration: 10, resolution: "1080p", aspect_ratio: "9:16"}),
});
const d = await r.json();
console.log(JSON.stringify(d, null, 2));
