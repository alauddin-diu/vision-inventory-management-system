import{aH as i,L as s,D as d,R as r,a as n,P as v,aq as g}from"./index-0d19177e.js";import{i as t,v as h}from"./BaseContext-b2603304-d1129fb6.js";import{e as m}from"./IconEdit-d5d0707d-e9613b1d.js";var p=t("device-floppy","IconDeviceFloppy",[["path",{d:"M6 4h10l4 4v10a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2",key:"svg-0"}],["path",{d:"M12 14m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0",key:"svg-1"}],["path",{d:"M14 4l0 4l-6 0l0 -4",key:"svg-2"}]]),u=t("moon-stars","IconMoonStars",[["path",{d:"M12 3c.132 0 .263 0 .393 0a7.5 7.5 0 0 0 7.92 12.446a9 9 0 1 1 -8.313 -12.454z",key:"svg-0"}],["path",{d:"M17 4a2 2 0 0 0 2 2a2 2 0 0 0 -2 2a2 2 0 0 0 -2 -2a2 2 0 0 0 2 -2",key:"svg-1"}],["path",{d:"M19 11h2m-1 -1v2",key:"svg-2"}]]),f=t("sun","IconSun",[["path",{d:"M12 12m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0",key:"svg-0"}],["path",{d:"M3 12h1m8 -9v1m8 8h1m-9 8v1m-6.4 -15.4l.7 .7m12.1 -.7l-.7 .7m0 11.4l.7 .7m-12.1 -.7l-.7 .7",key:"svg-1"}]]);function M(){const{colorScheme:a,toggleColorScheme:o}=i();return s.jsx(d,{position:"center",children:s.jsx(r,{onClick:()=>o(),size:"lg",sx:e=>({color:e.colorScheme==="dark"?e.colors.yellow[4]:e.colors.blue[6]}),children:a==="dark"?s.jsx(f,{}):s.jsx(u,{})})})}function j({setEditing:a,editing:o,disabled:e,saveIcon:l}){return l=l||s.jsx(p,{}),s.jsx(r,{onClick:()=>a(),disabled:e,children:o?l:s.jsx(m,{})})}function S(){const[a,o]=n.useState(null),[e,l]=v(c=>[c.language,c.setLanguage]);return n.useEffect(()=>{a!==null&&l(a)},[a]),n.useEffect(()=>{o(e)},[e]),s.jsx(g,{w:80,data:h,value:a,onChange:o})}export{S as C,M,j};