<template>
  <div id="app">
    <button v-on:click="save">Save</button>
    <button v-on:click="revert">Revert</button>
    <Theme v-for="(theme, key) in themes_data"
           :key="key"
           :name="key"
           :theme="theme"
    />
    <button v-on:click="save">Save</button>
    <button v-on:click="revert">Revert</button>
  </div>
</template>

<script>
import Theme from './components/Theme.vue'

export default {
  name: 'app',
  data: function(){
    return {
      themes_data: this.get_data_querystring()
    }
  },
  methods: {
    get_data_querystring: function(){
      var params = (new URL(document.location)).searchParams
      var raw_json = params.get('data')
      var themes_data = JSON.parse(raw_json)
      return themes_data
    },
    save: function(){
      /* It looks like there is a character limit on what can be
       * returned to python so the string gets split on the : and
       * reassembled in python.
       */
      var raw_json = JSON.stringify(this.themes_data)
      var broke = raw_json.split(':')
      for(var i=0; i<broke.length; i++){
        window.pywebview.api.save(broke[i])
      }
      window.pywebview.api.save('<!END!>')
    },
    revert: function(){
      this.themes_data = this.get_data_querystring()
    },
  },
  components: {
    Theme
  },
}
</script>

<style>
body{
  color: #BFBFBF;
  background-color: #1E1E1E;
  font-family: mono;
  margin: 20px;
}
</style>

<style scoped>
button {
  float: right;
  /* margin: 0 20px 20px 0; */
}
</style>
