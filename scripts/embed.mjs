import { initModel } from "@energetic-ai/embeddings";
import { modelSource } from "@energetic-ai/model-embeddings-en";
import fs from "fs";
function parseCSV(t){const rows=[];let i=0,f="",row=[],q=false;for(;i<t.length;i++){const c=t[i];if(q){if(c=='"'){if(t[i+1]=='"'){f+='"';i++}else q=false}else f+=c}else if(c=='"')q=true;else if(c==','){row.push(f);f=""}else if(c=='\n'){row.push(f);rows.push(row);row=[];f=""}else if(c!='\r')f+=c}if(f||row.length){row.push(f);rows.push(row)}return rows.slice(1).filter(r=>r.length==2)}
const model = await initModel(modelSource);
for (const split of ["train","test"]) {
  const rows = parseCSV(fs.readFileSync(split+".csv","utf8"));
  const out = [];
  for (let i=0;i<rows.length;i+=200){ const e=await model.embed(rows.slice(i,i+200).map(r=>r[0])); out.push(...e); }
  fs.writeFileSync(split+".json", JSON.stringify({texts:rows.map(r=>r[0]),labels:rows.map(r=>r[1]),emb:out.map(v=>Array.from(v).map(x=>+x.toFixed(5)))}));
  console.log(split, rows.length, out[0].length);
}
