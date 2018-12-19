
<template>
  <div>
    <h2 class="theme_title">{{name}}</h2>
    <Prompt :d="theme" />
    <table>
      <Segment name="sink" :d="theme.sink" />
      <Segment name="virt" :d="theme.virt" />
      <Segment name="user" :d="theme.user" />
      <Segment name="path" :d="theme.path" />
      <Segment name="ssh" :d="theme.ssh" />
      <Segment name="time" :d="theme.time" />
      <Segment name="pipenv" :d="theme.pipenv" />
      <Segment name="dollar" :d="theme.dollar" />
    </table>
  </div>
</template>


<script>
import Segment from './Segment.vue'
import Prompt from './Prompt.vue'
export default {
  props: ['name', 'theme'],
  components: {
    Segment,
    Prompt,
  }
}

</script>


<style scoped>
div{
  margin-bottom: 3em;
}
h2{
  color: white;
}
hr{
  border-bottom: 1px solid green;
  border-top: 0;
}
</style>
