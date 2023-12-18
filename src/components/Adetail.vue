<template>
<div class="row col-md-9">
    <div class="col-md-9">
        <MD :file_path="file_path" v-on:right_list_emit="right_list_emit"
            data-bs-spy="scroll" data-bs-target="#navbar" data-bs-smooth-scroll="true"
        ></MD>
        <div class="comment"></div>
    </div>
    <div class="col-md-3">
        <nav id="right-list" class="position-fixed flex-column align-items-stretch right-list">
            <nav class="nav nav-pills flex-column" v-for="group1 in right_list.c" :key="group1" >
                <div v-for="group2 in group1.c" :key="group2">
                    <a class="nav-link right-list-item" :href="'#'+group2.t">{{group2.n}}</a>
                    <nav class="nav nav-pills flex-column" v-for="group3 in group2.c" :key="group3">
                        <a class="nav-link right-list-item" :href="'#'+group3.t"><span class="place"/>{{group3.n}}</a> 
                    </nav>
                </div>
            </nav>
        </nav>
    </div>
</div>
</template>

<script>
import MD from './MD.vue'
import * as bootstrap from 'bootstrap';

export default {
    name : 'Adetail',
    data() {
        return{
            result: null,
            file_path: "",
            right_list: [],
            anchor_list: [],
            show: [],
            dic: this.$route.params.dic,
            full_height: document.documentElement.clientHeight,
        }
    },
    components: {
        MD,
    },
    created() {
        this.dic = this.$route.path.split('/')[1]
        this.file_path = '/' + this.dic +'/'+this.$route.params.file[0]+'/'+this.$route.params.file[1]
    },
    mounted() {
        const that = this
        window.addEventListener('scroll',this.scrollHandle)
        window.onresize = () => {
            return (() => {
                window.full_height = document.documentElement.clientHeight
                that.full_height = window.full_height
            })()
        }
        this.scrollSpyInstance = new bootstrap.ScrollSpy(document.body, {
            target: '#navbar',
            offset: 150,
        });
    },
    watch : {
        $route () {
            document.documentElement.scrollTop = 0;
            if(this.$route.params.file !== undefined) {
                this.file_path = '/' + this.dic +'/'+this.$route.params.file[0]+'/'+this.$route.params.file[1]
            }
        },
        full_height (val) {
            if(!this.timer) {
                this.full_height = val
                this.timer = true
                let that = this
                setTimeout(function (){
                    that.timer = false
                },400)
            }
        },
    },
    methods: {
        right_list_emit(right_list) {
            this.right_list = right_list
            this.convertId2Anchor(this.right_list.c[0], 3)
            this.scrollSpyInstance.refresh()
        },
        convertId2Anchor(list, n) {
            if ( --n == 0) return
            for (let l1 in list.c) {
                let tmp = list.c[l1].n.replace(/\s/g, '-').replace(/&/g, '').toLowerCase()
                let is_first = true
                while (this.anchor_list.includes(tmp)) {
                    if (is_first) {
                        tmp += '-1'
                        is_first = false
                    } else {
                        let num = tmp.split('-').pop()
                        num = parseInt(num, 10)+1
                        tmp = tmp.substring(0, tmp.lastIndexOf('-')) + '-' + num;
                    }
                }

                this.anchor_list.push(tmp)
                list.c[l1].t = tmp
                this.convertId2Anchor(list.c[l1])
            }
        },
    },
}
</script>

<style lang="scss">
#right-list {
    overflow: auto;

    .right-list-item {
        border-left-color: $color9;
        border-left-width: 0.3rem;
        border-left-style: solid;
        border-radius: 0;
        padding-left: 1rem;
        text-decoration: none;
        color: $color9;
        cursor: pointer;
    }

    .active {
        color: $color7;
        background-color: $color9;
    }

    .place {
        margin-left: 1.5rem;
    }

}
.comment {
    height: 30rem;
}
</style>
