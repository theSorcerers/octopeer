class Api::MouseScrollEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:mouse_scroll_event).permit(:viewport_x, :viewport_y, :session_id, :created_at)
  end
end
