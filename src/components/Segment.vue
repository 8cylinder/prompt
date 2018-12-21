
<template>
  <tr>
    <td><strong>{{name}}</strong></td>

    <td>fg: <input v-model="d.fg" type="color"></td>
    <td>bg: <input v-model="d.bg" type="color"></td>

    <td>
      <span class="off"
            v-bind:class="{on: d.bold}"
            v-on:click="toggle_bold()">Bold</span>
    </td>
    <td>
      <span class="off"
            v-bind:class="{on: d.italic}"
            v-on:click="toggle_italic()">Italic</span>
    </td>
    <td>
      <span class="off"
            v-bind:class="{on: d.underline}"
            v-on:click="toggle_ul()">Underline</span>
    </td>
  </tr>
</template>


<script>
export default{
  props: ['name', 'd'],
  methods: {
    toggle_bold: function(){
      this.d.bold = !this.d.bold
    },
    toggle_italic: function(){
      this.d.italic = !this.d.italic
    },
    toggle_ul: function(){
      this.d.underline = !this.d.underline
    },
  },
}
</script>


<style scoped>
p {
  margin: 0;
  margin-bottom: 0.5em;
}
strong{
  display: inline-block;
}
td{
  padding: 2px 10px;
}
span{
  cursor: pointer;
}
</style>
<style>
input {
  padding: 0px;
  height: 20px;
  width: 39px;
  /* background-color: #1e1e1e; */
  border: 0;
}
.on{
  color: white !important;
  font-weight: bold;
  text-decoration: underline;
}
.off{
  color: grey;
}
td:hover{
  background-color: #393939;
}
tr:hover{
  background-color: #2c2c2c;
}
</style>
