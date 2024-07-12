document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('modal');
    const daysContainer = document.getElementById('daysContainer');
    const closeBtn = document.querySelector('.close');
    const monthYear = document.getElementById('monthYear');
    const prevMonthBtn = document.getElementById('prevMonth');
    const nextMonthBtn = document.getElementById('nextMonth');
    const addEventBtn = document.getElementById('addEventBtn');
    const eventNameInput = document.getElementById('eventNameInput');
    const eventTimeInput = document.getElementById('eventTimeInput');
    const eventsList = document.getElementById('eventsList');

    let currentDate = new Date();
    let currentMonth = currentDate.getMonth();
    let currentYear = currentDate.getFullYear();
    let events = JSON.parse(localStorage.getItem('events')) || {};

    const generateCalendar = () => {
        const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
        const firstDayOfMonth = new Date(currentYear, currentMonth, 1).getDay();
        let daysHtml = '';

        for (let i = 0; i < firstDayOfMonth; i++) {
            daysHtml += '<div class="day empty"></div>';
        }

        for (let i = 1; i <= daysInMonth; i++) {
            const dateKey = `${currentYear}-${currentMonth + 1}-${i}`;
            const event = events[dateKey];
            daysHtml += `
                <div class="day" data-day="${i}">
                    ${i}
                    ${event ? `<div class="event">${event.name} - ${event.time}</div>` : ''}
                </div>
            `;
        }

        daysContainer.innerHTML = daysHtml;
        monthYear.textContent = `${getMonthName(currentMonth)} ${currentYear}`;
    };

    const getMonthName = (monthIndex) => {
        const months = [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ];
        return months[monthIndex];
    };

    const showEvents = () => {
        eventsList.innerHTML = '';
        for (const date in events) {
            const eventDate = new Date(date);
            if (eventDate.getMonth() === currentMonth && eventDate.getFullYear() === currentYear) {
                const day = eventDate.getDate();
                const month = eventDate.getMonth() + 1;
                const formattedDate = `${day}/${month < 10 ? '0' + month : month}`;
                const event = events[date];
                eventsList.innerHTML += `
                    <li data-date="${date}">
                        ${formattedDate} - ${event.name} - ${event.time}
                        <button class="editEventBtn">Editar</button>
                        <button class="deleteEventBtn">Eliminar</button>
                    </li>
                `;
            }
        }
    };

    const updateLocalStorage = () => {
        localStorage.setItem('events', JSON.stringify(events));
    };

    const handleModalClose = () => {
        modal.style.display = 'none';
        eventNameInput.value = '';
        eventTimeInput.value = '';
    };

    prevMonthBtn.addEventListener('click', () => {
        currentMonth--;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        }
        generateCalendar();
        showEvents();
    });

    nextMonthBtn.addEventListener('click', () => {
        currentMonth++;
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        generateCalendar();
        showEvents();
    });

    daysContainer.addEventListener('click', (event) => {
        if (event.target.classList.contains('day')) {
            modal.style.display = 'block';
            addEventBtn.dataset.day = event.target.getAttribute('data-day');
        }
    });

    closeBtn.addEventListener('click', handleModalClose);

    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            handleModalClose();
        }
    });

    addEventBtn.addEventListener('click', () => {
        const day = addEventBtn.dataset.day;
        const eventName = eventNameInput.value.trim();
        let eventTime = eventTimeInput.value.trim();

        if (eventName && isValidTime(eventTime)) {
            const dateKey = `${currentYear}-${currentMonth + 1}-${day}`;
            eventTime = formatTime(eventTime);
            events[dateKey] = { name: eventName, time: eventTime };
            updateLocalStorage();
            generateCalendar();
            showEvents();
            handleModalClose();
        } else {
            alert('Por favor ingrese un nombre de evento válido y un horario en formato HH:MM.');
        }
    });

    const isValidTime = (time) => {
        const regex = /^([01]\d|2[0-3]):?([0-5]\d)$/;
        return regex.test(time);
    };

    const formatTime = (time) => {
        const parts = time.split(':');
        return `${parts[0].padStart(2, '0')}:${parts[1].padStart(2, '0')}`;
    };

    eventsList.addEventListener('click', (event) => {
        const parent = event.target.parentElement;
        const date = parent.dataset.date;

        if (event.target.classList.contains('editEventBtn')) {
            const newName = prompt('Editar nombre del evento:', events[date].name);
            const newTime = prompt('Editar horario del evento:', events[date].time);

            if (newName !== null && newTime !== null) {
                events[date].name = newName.trim();
                events[date].time = formatTime(newTime.trim());
                updateLocalStorage();
                generateCalendar();
                showEvents();
            }
        }

        if (event.target.classList.contains('deleteEventBtn')) {
            delete events[date];
            updateLocalStorage();
            generateCalendar();
            showEvents();
        }
    });

    generateCalendar();
    showEvents();
});
