const BASE_URL = "https://moodmate-6-z0a4.onrender.com";

export async function login(name) {
    const res = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name }),
    });
    return res.json();
}

export async function logMood(userId, mood) {
    const res = await fetch(`${BASE_URL}/moods`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: userId, mood }),
    });
    return res.json();
}

export async function getMoodLogs(username) {
    const res = await fetch(`${BASE_URL}/moods/${username}`);
    return res.json();
}

export async function deleteMood(moodId) {
    const res = await fetch(`${BASE_URL}/moods/${moodId}`, {
        method: "DELETE",
    });

    if (!res.ok) {
        throw new Error("Failed to delete mood");
    }

    return res.json();
}
