import{L as t,D as c,a as r,I as l}from"./index-0d19177e.js";import{D as d,p as e}from"./BaseContext-b2603304-d1129fb6.js";import{n as b}from"./Placeholder-d8632411-711021b4.js";import{o as p}from"./StylishText-56caa9d1-838dbefd.js";import{e as n}from"./notifications-507207d9-c05c5d70.js";import{R as _,I as m}from"./Vision_IMSTable-136a1ca9-ce527cb7.js";import"./IconSearch-a226eee4-73f8e550.js";import"./globalStyle-ed485bee-3719433e.js";function u({str:i,len:a=100}){if(i=i.toString(),i.length<=a)return i;let o=Math.floor(a/2-1);return i.slice(0,o)+"..."+i.slice(-o)}function h(){return[{accessor:"name",sortable:!0,title:e._({id:"vgP+9p"}),render:function(i){return t.jsx(m,{src:i.thumbnail||i.image,text:i.name,link:""})}},{accessor:"IPN",title:e._({id:"3wXEsN"}),sortable:!0,switchable:!0},{accessor:"units",sortable:!0,title:e._({id:"QrhaVg"}),switchable:!0},{accessor:"description",title:e._({id:"Nu4oKW"}),sortable:!0,switchable:!0},{accessor:"category",title:e._({id:"K7tIrx"}),sortable:!0,render:function(i){return u({str:i.category_detail.pathstring})}},{accessor:"total_in_stock",title:e._({id:"blbbPS"}),sortable:!0,switchable:!0},{accessor:"price_range",title:e._({id:"YA4hwj"}),sortable:!1,switchable:!0,render:function(i){return"-- price --"}},{accessor:"link",title:e._({id:"yzF66j"}),switchable:!0}]}function y(){return[{name:"active",label:e._({id:"F6pfE9"}),description:e._({id:"PHri/6"}),type:"boolean"},{name:"assembly",label:e._({id:"WL36Yh"}),description:e._({id:"oQzKsK"}),type:"boolean"},{name:"cascade",label:e._({id:"NgZniC"}),description:e._({id:"5JhtGd"}),type:"boolean"},{name:"component",label:e._({id:"dK3Z9j"}),description:e._({id:"oO7QIX"}),type:"boolean"},{name:"trackable",label:e._({id:"y6MnU0"}),description:e._({id:"MbixSq"}),type:"boolean"},{name:"has_units",label:e._({id:"YyRdJQ"}),description:e._({id:"WyFVby"}),type:"boolean"},{name:"has_ipn",label:e._({id:"c9/Fqb"}),description:e._({id:"jh/Aa+"}),type:"boolean"},{name:"has_stock",label:e._({id:"JqmfuT"}),description:e._({id:"6Kd+HK"}),type:"boolean"},{name:"low_stock",label:e._({id:"UgdO7s"}),description:e._({id:"GDYPCw"}),type:"boolean"},{name:"purchaseable",label:e._({id:"TW9g28"}),description:e._({id:"KMdl2R"}),type:"boolean"},{name:"salable",label:e._({id:"/3xNJ4"}),description:e._({id:"V5i7hf"}),type:"boolean"},{name:"virtual",label:e._({id:"ksX7Wx"}),description:e._({id:"QDTpY6"}),type:"choice",choices:[{value:"true",label:e._({id:"ksX7Wx"})},{value:"false",label:e._({id:"+SkaI8"})}]}]}function f(i){return{...i,category_detail:!0}}function x({params:i={}}){let a=r.useMemo(()=>f(i),[]),o=r.useMemo(()=>h(),[]),s=r.useMemo(()=>y(),[]);return a.category_detail=!0,t.jsx(_,{url:"part/",enableDownload:!0,tableKey:"part-table",printingActions:[t.jsx(l,{onClick:n,children:"Hello"}),t.jsx(l,{onClick:n,children:"World"})],params:a,columns:o,customFilters:s})}function D(){return t.jsxs(t.Fragment,{children:[t.jsxs(c,{children:[t.jsx(p,{children:t.jsx(d,{id:"pmRbKZ"})}),t.jsx(b,{})]}),t.jsx(x,{})]})}export{D as default};