import{L as e,D as c,a,R as m,ae as b}from"./index-0d19177e.js";import{D as p,p as i}from"./BaseContext-b2603304-d1129fb6.js";import{n as f}from"./Placeholder-d8632411-711021b4.js";import{o as x}from"./StylishText-56caa9d1-838dbefd.js";import{e as l}from"./notifications-507207d9-c05c5d70.js";import{R as h,I as j}from"./Vision_IMSTable-136a1ca9-ce527cb7.js";import{e as _}from"./IconEdit-d5d0707d-e9613b1d.js";import{e as k}from"./IconTrash-0f9cb02d-5e67fec3.js";import"./IconSearch-a226eee4-73f8e550.js";import"./globalStyle-ed485bee-3719433e.js";function n({icon:t,color:o="black",tooltip:r="",disabled:s=!1,size:d=18,onClick:u}){return e.jsx(m,{disabled:s,radius:"xs",color:o,size:d,onClick:u,children:e.jsx(b,{disabled:!r,label:r,position:"left",children:t})})}function g(){return[{accessor:"part",sortable:!0,title:i._({id:"vgP+9p"}),render:function(t){let o=t.part_detail;return e.jsx(j,{src:o.thumbnail||o.image,text:o.name,link:""})}},{accessor:"part_detail.description",sortable:!1,switchable:!0,title:i._({id:"Nu4oKW"})},{accessor:"quantity",sortable:!0,title:i._({id:"blbbPS"})},{accessor:"status",sortable:!0,switchable:!0,filter:!0,title:i._({id:"uAQUqI"})},{accessor:"batch",sortable:!0,switchable:!0,title:i._({id:"rsx3xA"})},{accessor:"location",sortable:!0,switchable:!0,title:i._({id:"wJijgU"}),render:function(t){return t.location}},{accessor:"actions",title:i._({id:"7L01XJ"}),sortable:!1,render:function(t){return e.jsxs(c,{position:"right",spacing:5,noWrap:!0,children:[e.jsx(n,{color:"green",icon:e.jsx(_,{}),tooltip:"Edit stock item",onClick:()=>l()}),e.jsx(n,{color:"red",tooltip:"Delete stock item",icon:e.jsx(k,{}),onClick:()=>l()})]})}}]}function w(t){return{...t,part_detail:!0,location_detail:!0}}function v(){return[{name:"test_filter",label:i._({id:"VikQny"}),description:i._({id:"ay6lVf"}),type:"choice",choiceFunction:()=>[{value:"1",label:"One"},{value:"2",label:"Two"},{value:"3",label:"Three"}]}]}function y({params:t={}}){let o=a.useMemo(()=>w(t),[]),r=a.useMemo(()=>g(),[]),s=a.useMemo(()=>v(),[]);return e.jsx(h,{url:"stock/",tableKey:"stock-table",enableDownload:!0,enableSelection:!0,params:o,columns:r,customFilters:s})}function R(){return e.jsxs(e.Fragment,{children:[e.jsxs(c,{children:[e.jsx(x,{children:e.jsx(p,{id:"Jbck4N"})}),e.jsx(f,{})]}),e.jsx(y,{})]})}export{R as default};
