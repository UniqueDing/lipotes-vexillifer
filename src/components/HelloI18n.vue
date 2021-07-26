<template>
  <p>{{ t('hello') }}</p>
</template>

<script>
import { defineComponent } from 'vue'
import { useI18n } from 'vue-i18n/index'

export default defineComponent({
  name: 'HelloI18n',
  setup() {
    const { t } = useI18n({
      inheritLocale: true,
      /* useScope: 'local' */
    })

    // Something todo ..

    return { t }
  }
})
</script>

<i18n-bak>
{
  "aen": {
    "hello": "Hello i18n in SFC!"
  }
}
</i18n-bak>
