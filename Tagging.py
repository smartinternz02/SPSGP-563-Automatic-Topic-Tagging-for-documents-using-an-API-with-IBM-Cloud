import http.client

conn = http.client.HTTPSConnection("twinword-topic-tagging.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "9029b8132cmshe699ad0a74455b5p19970djsnc8e2f66c61b7",
    'x-rapidapi-host': "twinword-topic-tagging.p.rapidapi.com"
    }

conn.request("GET", "/generate/?text=Computer%20science%20is%20the%20scientific%20and%20practical%20approach%20to%20computation%20and%20its%20applications.%20It%20is%20the%20systematic%20study%20of%20the%20feasibility%2C%20structure%2C%20expression%2C%20and%20mechanization%20of%20the%20methodical%20procedures%20(or%20algorithms)%20that%20underlie%20the%20acquisition%2C%20representation%2C%20processing%2C%20storage%2C%20communication%20of%2C%20and%20access%20to%20information%2C%20whether%20such%20information%20is%20encoded%20as%20bits%20in%20a%20computer%20memory%20or%20transcribed%20in%20genes%20and%20protein%20structures%20in%20a%20biological%20cell.%20An%20alternate%2C%20more%20succinct%20definition%20of%20computer%20science%20is%20the%20study%20of%20automating%20algorithmic%20processes%20that%20scale.%20A%20computer%20scientist%20specializes%20in%20the%20theory%20of%20computation%20and%20the%20design%20of%20computational%20systems.", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))