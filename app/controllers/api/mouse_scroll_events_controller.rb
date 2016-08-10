class Api::MouseScrollEventsController < ApplicationController
  include TimeHelper
  include Showable
  include Indexable
  include Createable

  private

  def mouse_scroll_event_params
    params.require(:mouse_scroll_event).permit(:viewport_x, :viewport_y, :session_id, :created_at)
  end
end
