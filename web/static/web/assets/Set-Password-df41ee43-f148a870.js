import{a as h,L as e,l as g,m as _,U as p,g as f,aG as x,G as v,b as j}from"./index-0d19177e.js";import{F as o,p as a,Z,D as c}from"./BaseContext-b2603304-d1129fb6.js";import{h as k,c as F,g as b,A as G}from"./DesktopAppView-6f26ab52-fe364a3c.js";import{G as L}from"./use-form-5049279f-ad64b2d3.js";function H(){const i=L({initialValues:{password:""}}),[n]=k(),t=F(),r=n.get("token"),d=n.get("uid");function m(){o.show({title:a._({id:"eV2FZ+"}),message:a._({id:"uAHzZQ"}),color:"red"}),t("/login")}function l(s){o.show({title:a._({id:"WhimMi"}),message:(s==null?void 0:s.new_password2)||(s==null?void 0:s.new_password1)||(s==null?void 0:s.token),color:"red"})}h.useEffect(()=>{(!r||!d)&&(o.show({title:a._({id:"+5xxir"}),message:a._({id:"KuLTFa"}),color:"red"}),t("/login"))},[r]);function w(){j.post(b(G.user_reset_set),{uid:d,token:r,new_password1:i.values.password,new_password2:i.values.password},{headers:{Authorization:""}}).then(s=>{s.status===200?(o.show({title:a._({id:"Hw2MHB"}),message:a._({id:"+p8fKY"}),color:"green",autoClose:!1}),t("/login")):l(s.data)}).catch(s=>{var u;s.response.status===400&&((u=s.response.data)==null?void 0:u.token)=="Invalid value"?m():l(s.response.data)})}return e.jsx(Z,{children:e.jsx(g,{mih:"100vh",children:e.jsx(_,{w:"md",miw:425,children:e.jsxs(p,{children:[e.jsx(f,{children:e.jsx(c,{id:"V/e7nf"})}),e.jsx(p,{children:e.jsx(x,{required:!0,label:a._({id:"8ZsakT"}),description:a._({id:"Wr5sDQ"}),...i.getInputProps("password")})}),e.jsx(v,{type:"submit",onClick:w,children:e.jsx(c,{id:"F+gz9Z"})})]})})})})}export{H as default};
