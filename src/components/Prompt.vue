<!-- PROMPT -->

<template>
  <p>
    <span v-bind:style="styles('sink')">[project]</span>
    <span v-bind:style="styles('virt')">[virt]</span>
    <span v-bind:style="styles('ssh')">[ssh]</span>
    <span v-bind:style="styles('pipenv')">[pip]</span>
    <span v-bind:style="styles('time')">12:00am</span>
    <span v-bind:style="styles('user')">user@server</span>
    <span v-bind:style="styles('path')">~/projects/someproject/src/compile</span>
    <br><span v-bind:style="styles('dollar')">❖</span>
    <span class="command">emacs -nw -q</span>
    <br><br>
    <span v-bind:style="styles('sink')">[project]</span>
    <span v-bind:style="styles('user')">user@server</span>
    <span v-bind:style="styles('path')">~/projects/someproject/src/compile</span>
    <br><span v-bind:style="styles('dollar')">❖</span>
    <span class="command">ls --long --all</span>
  </p>
</template>


<script>
export default{
  props: ['d'],
  methods: {
    styles: function(name){
      return {
        color: this.d[name].fg,
        backgroundColor: this.d[name].bg,
        fontWeight: (this.d[name].bold) ? 'bold' : '',
        fontStyle: (this.d[name].italic) ? 'italic' : '',
        textDecoration: (this.d[name].underline) ? 'underline' : '',
      }
    },
  },
}
</script>


<style scoped>
p{
  background-color: black;
  color: white;
  font-family: mono;
  padding: 10px 10px 10px 20px;
  white-space: nowrap;
  overflow: hidden;
}
span{
  margin-right: 0.5em;
}
.command{
  color: #BABDB6
}
</style>
