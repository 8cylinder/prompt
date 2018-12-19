
<template>
  <tr>
    <td><strong>{{name}}</strong></td>
    <td>fg: {{d.fg}}</td>
    <td>bg: {{d.bg}}</td>
    <td><span class="off" v-bind:class="{on: d.bold}" v-on:click="toggle_bold()">Bold</span></td>
    <td><span class="off" v-bind:class="{on: d.italic}" v-on:click="toggle_italic()">Italic</span></td>
    <td><span class="off" v-bind:class="{on: d.underline}" v-on:click="toggle_ul()">Underline</span></td>
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
  /* min-width: 55px; */
  /* margin-right: 1em; */
}
td{
  padding: 2px 10px;
}
</style>
<style>
.on{
  color: white !important;
  font-weight: bold;
  text-decoration: underline;
}
.off{
  color: grey;
}
</style>
