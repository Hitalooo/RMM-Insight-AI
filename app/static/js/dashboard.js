document.addEventListener("DOMContentLoaded", ()=>{

    const counters=document.querySelectorAll(".counter");

    counters.forEach(counter=>{

        const target=parseInt(counter.dataset.target);

        let value=0;

        const speed=Math.max(1,target/60);

        const update=()=>{

            value+=speed;

            if(value>=target){

                counter.innerText=target;

                return;
            }

            counter.innerText=Math.floor(value);

            requestAnimationFrame(update);

        };

        update();

    });

});