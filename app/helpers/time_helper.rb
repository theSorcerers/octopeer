module TimeHelper
  def format_time(event)
    begin
      params[event][:created_at] = Time.parse(params[event][:created_at]).utc.to_f
    rescue
      params[event][:created_at] = Time.at(params[event][:created_at].to_f).utc
    end
  end
end
