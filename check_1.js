
    // Lightweight fallback submit handler â€” minimal and resilient.
    (function(){
      try{
        const f = document.getElementById('auth-form');
        if(!f) return;
        f.addEventListener('submit', async function(e){
          e.preventDefault();
          const email = (document.getElementById('email')||{}).value?.trim?.() || '';
          const password = (document.getElementById('password')||{}).value || '';
          if(!email || !password){ alert('Enter email and password'); return; }
          try{
            const r = await fetch('/api/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({email,password}) });
            const j = await r.json();
            if(j && j.success){ localStorage.setItem('currentUser', JSON.stringify(j.user)); location.reload(); }
            else { alert(j && j.message ? j.message : 'Login failed'); }
          }catch(err){ console.error('Fallback login error', err); alert('Server error â€” check backend.'); }
        });
      }catch(ex){ console.error('Auth fallback init failed', ex); }
    })();
    
