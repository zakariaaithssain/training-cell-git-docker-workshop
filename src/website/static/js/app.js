let cartCount = 0;

function showNotification(message, type = 'success') {
    const container = document.getElementById('notification-container');
    const notif = document.createElement('div');
    notif.className = `notification ${type}`;
    notif.innerText = message;
    
    container.appendChild(notif);
    
    setTimeout(() => {
        notif.style.animation = 'fadeOut 0.3s ease-out forwards';
        setTimeout(() => notif.remove(), 300);
    }, 3000);
}

async function buyProduct(productId, btnElement) {
    btnElement.disabled = true;
    const originalText = btnElement.innerText;
    btnElement.innerText = "Traitement...";

    try {
        const response = await fetch(`/api/buy/${productId}`, {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (response.ok) {
            cartCount++;
            document.getElementById('cart-count').innerText = cartCount;
            showNotification(`Succès : ${data.message}`);
            
            // Disable ALL buy buttons temporarily while reloading
            const allBtns = document.querySelectorAll('.btn-buy');
            allBtns.forEach(btn => {
                btn.disabled = true;
                btn.style.cursor = 'wait';
            });
            
            setTimeout(() => {
                window.location.reload();
            }, 1200);
            
            return; // Exit early
        } else {
            showNotification(`Erreur : ${data.detail}`, 'error');
        }
    } catch (error) {
        showNotification("Erreur réseau", 'error');
    }
    
    btnElement.disabled = false;
    btnElement.innerText = originalText;
}

async function cancelProduct(productId, btnElement) {
    btnElement.disabled = true;
    const originalText = btnElement.innerText;
    btnElement.innerText = "Annulation...";

    try {
        const response = await fetch(`/api/cancel_buy/${productId}`, {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (response.ok) {
            if(cartCount > 0) cartCount--;
            document.getElementById('cart-count').innerText = cartCount;
            showNotification(`Succès : ${data.message}`, 'success');
            
            // Disable all buttons while reloading
            const allBtns = document.querySelectorAll('.btn-buy');
            allBtns.forEach(btn => {
                btn.disabled = true;
                btn.style.cursor = 'wait';
            });
            
            setTimeout(() => {
                window.location.reload();
            }, 1200);
            
            return;
        } else {
            showNotification(`Erreur : ${data.detail}`, 'error');
        }
    } catch (error) {
        showNotification("Erreur réseau", 'error');
    }
    
    btnElement.disabled = false;
    btnElement.innerText = originalText;
}
